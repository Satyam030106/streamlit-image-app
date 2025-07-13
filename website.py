import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title("hello cutu")
name=st.text_input("Enter your name here my love:")
if name:
    st.write(f"I LOVE YOU SO MUCHH {name}")

LOVE=st.slider("How much you love me?",0,100,25)
st.write(f"You love me {LOVE}/100")  

options = ["Bhondulaal","Ghonchulaal","Kallu","Bihari"]
choice= st.selectbox("Choose what you are;",options)
st.write(f"YOU are {choice}")


# Load an existing image
image = Image.open("WhatsApp Image 2025-07-13 at 12.17.27_fc478ca3.jpg")  # Make sure this image is in the same folder

# Display the image
st.image(image, caption=f'This is an {choice} image.', use_column_width=True)
