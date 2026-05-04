import streamlit as st
import numpy as np
import pickle
import cv2
from PIL import Image
from skimage.feature import hog

st.set_page_config(page_title="Cat vs Dog", layout="centered")

st.title("🐶🐱 Cat vs Dog Classifier")

@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

IMG_SIZE = 128

uploaded_file = st.file_uploader(
    "Upload Image", 
    type=["jpg", "png", "jpeg"],
    key="uploader"
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image")

    if st.button("Predict", key="predict_btn"):
        img = np.array(image)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        features = hog(
            gray,
            orientations=9,
            pixels_per_cell=(8, 8),
            cells_per_block=(2, 2),
            block_norm='L2-Hys'
        )

        prediction = model.predict([features])[0]

        if prediction == 0:
            st.success("🐱 Cat")
        else:
            st.success("🐶 Dog")