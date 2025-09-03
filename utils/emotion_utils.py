import numpy as np
from keras.models import load_model # type: ignore
import cv2

emotion_dict = {
    0: "Angry", 1: "Disgust", 2: "Fear",
    3: "Happy", 4: "Sad", 5: "Surprise", 6: "Neutral"
}

def load_emotion_model(model_path='models/emotion_model.h5'):
    return load_model(model_path)

def predict_emotion(face_img, model):
    face_img = cv2.resize(face_img, (48, 48))
    face_img = face_img.astype('float') / 255.0
    face_img = np.reshape(face_img, (1, 48, 48, 1))
    prediction = model.predict(face_img)
    return emotion_dict[np.argmax(prediction)]
