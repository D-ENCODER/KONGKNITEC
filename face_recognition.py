# Date    : 20/07/22 10:01 PM
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0

import numpy as np
import cv2
import os


# KNN CODE (START)
def distance(value_1, value_2):
    """
    Finds the distance between two points in terms of matrix(x1, y1) using Euclidian algorithm.
    :param value_2:
    :param value_1: :return Double:
    """
    return np.sqrt(((value_1 - value_2) ** 2).sum())


def knn(train, test, k=5):
    """
    K-nearest neighbour algorithm which performs the similarity test on the present data and the data that is in
    the file. :param train: :param test: :param k: :return Double:
    """
    dist = []
    for i in range(train.shape[0]):
        # Get the vector and label
        ix = train[i, :-1]
        iy = train[i, -1]
        # Compute the distance from test point
        d = distance(test, ix)
        dist.append([d, iy])
    # Sort based on distance and get top k
    dk = sorted(dist, key=lambda x: x[0])[:k]
    # Retrieve only the labels
    labels = np.array(dk)[:, -1]

    # Get frequencies of each label
    output = np.unique(labels, return_counts=True)
    # Find max frequency and corresponding label
    index = np.argmax(output[1])
    return output[0][index]


# KNN CODE (END)
# Object initialization for capturing live video frame by frame

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("Detectors/haarcascade_frontalface_alt.xml")

# Initializing variable for future use.
dataset_path = "./face_dataset/"
face_data = []
labels = []
class_id = 0
names = {}

# Dataset data retrieving
for fx in os.listdir(dataset_path):
    if fx.endswith('.npy'):
        names[class_id] = fx[:-4]
        data_item = np.load(dataset_path + fx)
        face_data.append(data_item)

        target = class_id * np.ones((data_item.shape[0],))
        class_id += 1
        labels.append(target)

face_dataset = np.concatenate(face_data, axis=0)
face_labels = np.concatenate(labels, axis=0).reshape((-1, 1))
print(face_labels.shape)
print(face_dataset.shape)
trainset = np.concatenate((face_dataset, face_labels), axis=1)
print(trainset.shape)

font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, frame = cap.read()
    # ret is boolean it is false if the frame is not recorded correctly and vice-versa.
    if ret is False:
        continue
    # Converting the frame to grayscale as face detection becomes easy in grayscale images than BGR images.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect multi faces in the image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # Getting the x and y co-ordinates of the face that is detected
    for face in faces:
        x, y, w, h = face
        # Get the face ROI
        offset = 5
        face_section = frame[y - offset:y + h + offset, x - offset:x + w + offset]
        face_section = cv2.resize(face_section, (100, 100))
        out = knn(trainset, face_section.flatten())
        # Draw rectangle in the original image
        cv2.putText(frame, names[int(out)], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)
    cv2.imshow("Faces", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# releasing the resources that were in use.
cap.release()
cv2.destroyAllWindows()
