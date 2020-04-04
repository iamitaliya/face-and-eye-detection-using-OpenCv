import cv2

# getting the files
face_classifier = cv2.CascadeClassifier(
    "haarcascade_frontalface_alt_tree.xml")
eye_classifier = cv2.CascadeClassifier(
    "haarcascade_eye.xml")


def detector(frame):
    face = face_classifier.detectMultiScale(frame)
    eye = eye_classifier.detectMultiScale(frame, 1.2, 15)

    for x, y, h, w in face:
        frame = cv2.rectangle(frame, (x, y), (x+w, x+h), (0, 0, 255))
        eyes = 0
        for a, b, c, d in eye:
            frame = cv2.rectangle(frame, (a, b), (a+c, b+d), (255, 0, 0))
            eyes += 1
            if eyes == 2:
                break

    cv2.imshow("frame", frame)
