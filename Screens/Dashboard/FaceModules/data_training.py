# Date    : 20-03-2023 17:25
# Author  : DENCODER (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0

import os
import pickle
import face_recognition


class TrainDataset:
    def __init__(self, parent):
        parent.configure(state="disabled")
        self.allFaceEncodings = {}
        for file in os.listdir("Dataset"):
            if not file.endswith(".jpg"):
                continue
            image = face_recognition.load_image_file("Dataset/" + file)
            user = file.split(".")[0]
            self.allFaceEncodings[str(user)] = face_recognition.face_encodings(image)[0]
        with open('Dataset/TrainedData/trained_dataset.dat', 'wb') as f:
            pickle.dump(self.allFaceEncodings, f)
        parent.configure(state="normal")
