import cv2
from utils.emotion_utils import load_emotion_model, predict_emotion
from recommend_music import play_music

model = load_emotion_model()
cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
detected = False

while not detected:
    ret, frame = cap.read()
    if not ret:
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        emotion = predict_emotion(roi_gray, model)
        print(f"Detected Emotion: {emotion}")
        play_music(emotion)
        detected = True
        break

    cv2.imshow('Mood Detection - Press Q to quit', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
