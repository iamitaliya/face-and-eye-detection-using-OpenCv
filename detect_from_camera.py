import cv2
from detector import detector

# starts the camera and displays frames
cap = cv2.VideoCapture(0)


while True:
    read, frame = cap.read()

    if not read:
        print("There is no frame to read")
        break

    frame = cv2.flip(frame, 1)

    # the detector function
    detector(frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
