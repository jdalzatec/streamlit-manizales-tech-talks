from io import StringIO

import streamlit
from h5py import File
from keras.models import load_model

from utils import predict

model = None
labels = []

model_file = streamlit.file_uploader("Model file uploader:")
if model_file:
    model = load_model(File(model_file))

labels_file = streamlit.file_uploader("Model labels uploader:")
if labels_file:
    lines = StringIO(labels_file.getvalue().decode()).readlines()
    for line in lines:
        index, *remaining = line.split()
        index = int(line[0])
        label = " ".join(remaining).strip()
        labels.append(label)


if model and labels:
    image = streamlit.camera_input("Webcam image")
    if image:
        with streamlit.spinner(text="Predicting ..."):
            prediction = predict(image, model)

        result = {label: probability for label, probability in zip(labels, prediction)}

        streamlit.json(result)
