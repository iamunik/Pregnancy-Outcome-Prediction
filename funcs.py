import streamlit as st
import os
import base64


def yes_no_to_binary(question, input_type):
    """Converts a Yes/No response to binary (0 or 1) using either radio or selectbox."""
    if input_type == "radio":
        response = st.radio(question, options=["No", "Yes"])
    elif input_type == "selectbox":
        response = st.selectbox(question, options=["No", "Yes"], index=0)
    else:
        raise ValueError("Invalid input type. Use 'radio' or 'selectbox'.")
    return 1 if response == "Yes" else 0


def open_picture(image_name):
    cwd = os.path.dirname(__file__)
    image_path = os.path.join(cwd, "image", image_name)
    image_path = os.path.abspath(image_path)
    file = open(image_path, "rb")
    images = base64.b64encode(file.read()).decode()
    return images
