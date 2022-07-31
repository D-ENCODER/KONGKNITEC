# Date    : 20/07/22 10:01 PM
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0

import cv2

# Object initialization to capture live video frame by frame
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(
    "Detectors/haarcascade_frontalface_alt.xml"
)

while True:
    ret, frame = cap.read()
    # Converting the frame to grayscale as face detection becomes easy in grayscale images than BGR images.
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # ret is boolean it is false if the frame is not recorded correctly and vice-versa.
    if ret is False:
        continue
    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)
    if len(faces) == 0:
        continue
    # Getting the x and y co-ordinates of the face found in the frame.
    for face in faces[:1]:
        x, y, w, h = face
        offset = 10
        face_offset = frame[y - offset : y + h + offset, x - offset : x + w + offset]
        face_selection = cv2.resize(face_offset, (100, 100))
        cv2.imshow("Face", face_selection)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("faces", frame)
    # If you press q then the command is terminated or else it continues the infinite loop.
    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord("q"):
        break

# Releasing the resources that were in use by the program.
cap.release()
cv2.destroyAllWindows()
