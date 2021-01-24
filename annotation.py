import os
import random
import streamlit as st
import streamlit.session_state as SessionState
from PIL import Image

script_path = os.path.dirname(__file__)
rel_path = 'images'
abs_file_path = script_path + '/' + rel_path
files = os.listdir(rel_path)

state = SessionState(
    annotations={},
    files=files,
    current_image='cat.1.jpg'
)


def load_next_image(annotation_response):
    state.annotations[state.current_image] = annotation_response
    random_index = random.randint(0, len(state.files) - 1)
    state.current_image = state.files[random_index]
    state.files.remove(state.current_image)


image_path = abs_file_path + '/' + state.current_image
image = Image.open(image_path)

st.title('Cat vs Dog: Image Annotation')

st.image(image, caption='Please input whether this is a dog or a cat')

annotation_response = st.selectbox(label='', options=['cat', 'dog'])
st.button(label='Next', on_click=lambda: load_next_image(annotation_response))


st.markdown('---')
st.header('Annotations')
st.write(state.__dict__)


if len(state.files) == 0:
    st.warning('Finished Annotation')
    st.stop()
