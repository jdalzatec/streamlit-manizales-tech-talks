import streamlit

from utils import load_model, predict, read_labels

model = None
labels = []

model_file = streamlit.file_uploader("Model file uploader:")
if model_file:
    model = load_model(model_file)

labels_file = streamlit.file_uploader("Model labels uploader:")
if labels_file:
    labels = read_labels(labels_file)


if model and labels:
    image = streamlit.camera_input("Webcam image")
    if image:
        with streamlit.spinner(text="Predicting ..."):
            prediction = predict(image, model)

        result = {label: probability for label, probability in zip(labels, prediction)}

        streamlit.json(result)
