import os
import random
import streamlit as st
from PIL import Image

script_path = os.path.dirname(__file__)
rel_path = 'images'
abs_file_path = script_path + '/' + rel_path
files = os.listdir(abs_file_path)

if 'initialized' not in st.session_state:
    st.session_state.annotations = {}
    st.session_state.files = files
    st.session_state.current_image = 'cat.1.jpg'
    st.session_state.initialized = True

# state = st.session_state

# state = st.beta_session_state(
#     annotations={},
#     files=files,
#     current_image='cat.1.jpg'
# )


def annotate():
    annotation_response = st.session_state.annotation_response
    st.session_state.annotations[st.session_state.current_image] = annotation_response
    random_index = random.randint(0, len(st.session_state.files) - 1)
    st.session_state.current_image = st.session_state.files[random_index]
    st.session_state.files.remove(st.session_state.current_image)


image_path = abs_file_path + '/' + st.session_state.current_image
image = Image.open(image_path)

st.title('Cat vs Dog: Image Annotation')

st.image(image, caption='Please input whether this is a dog or a cat')

annotation_response = st.selectbox(key='annotation_response', label='', options=['cat', 'dog'])
st.button(label='Next', on_change=annotate)


st.markdown('---')
st.header('Annotations')
st.write(st.session_state.annotations)


if len(st.session_state.files) == 0:
    st.warning('Finished Annotation')
    st.stop()
