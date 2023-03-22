# Date    : 20-03-2023 17:26
# Author  : DENCODER (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0

import pickle
from datetime import datetime
from tkinter import PhotoImage

import face_recognition
import customtkinter as ctk
import cv2
import numpy as np
from PIL import Image, ImageTk
import configure
from Backend.FirebaseServices.attendanceServices import AttendanceServices
from Backend.SqliteServices.attendance_sqlite_services import AttendanceSqliteServices
from Screens.Refactor.customWidgets import CustomWidgets


class FacialRecognition(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Facial Recognition")
        self.protocol("WM_DELETE_WINDOW", self.onClosing)
        self._icon = PhotoImage(file="Assets/logo.png")
        self.iconphoto(False, self._icon)
        self.geometry("650x550")
        self.configure(fg_color=configure.very_dark_gray)
        self.__attendanceFirebase = AttendanceServices()
        self.enrolls = []
        self.__frame = ctk.CTkFrame(self, fg_color=configure.very_dark_gray)
        # self.__label = ctk.CTkLabel(self.__frame, text_font=(configure.font, 20, "bold"))
        # self.__label.grid(row=0, column=0, sticky="nsew")
        self.__textarea = ctk.CTkTextbox(self.__frame, text_font=(configure.font, 15), corner_radius=10,
                                         width=600, fg_color=configure.very_dark_gray, height=450)
        self.__textarea.configure(state="disabled")
        self.__textarea.grid(row=1, column=0, sticky="nsew", pady=20, padx=25)
        self.__button = CustomWidgets.customButton(parent=self.__frame, text="Stop", command=self.onClosing)
        self.__button.grid(row=2, column=0, sticky="nsew", pady=20, padx=25)
        self.__frame.grid(row=0, column=0, sticky="nsew")
        self.__date = datetime.now().strftime("%d%m%Y")
        self.__attendancesql = AttendanceSqliteServices()
        self.__attendancesql.createTable(self.__date)
        self.__videoCapture = cv2.VideoCapture(0)
        with open('Dataset/TrainedData/trained_dataset.dat', 'rb') as f:
            self.all_face_encodings = pickle.load(f)
        self.__knownFaceNames = list(self.all_face_encodings.keys())
        self.__knownFaceEncodings = list(self.all_face_encodings.values())
        self.__faceLocations = []
        self.__faceEncodings = []
        self.__faceNames = []
        self.__recognize()

    def __recognize(self):
        # Grab a single frame of video
        _, frame = self.__videoCapture.read()
        # Only process every other frame of video to save time
        # if process_this_frame:
        # Resize frame of video to 1/4 size for faster face recognition processing
        smallFrame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgbSmallFrame = smallFrame[:, :, ::-1]
        # Find all the faces and face encodings in the current frame of video
        faceLocations = face_recognition.face_locations(rgbSmallFrame)
        faceEncodings = face_recognition.face_encodings(rgbSmallFrame, faceLocations)

        face_names = []
        for face_encoding in faceEncodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(self.__knownFaceEncodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = self.__knownFaceNames[first_match_index]
                name = 'A' + name

            # Or instead, use the known face with the smallest distance to the new face
            else:
                face_distances = face_recognition.face_distance(self.__knownFaceEncodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = self.__knownFaceNames[best_match_index]
                    name = 'A' + name

            if name != "Unknown":
                enrolls = list(self.__attendancesql.getEnrollment(self.__date))
                for i in enrolls:
                    enrolls[enrolls.index(i)] = i[0]
                if name not in enrolls:
                    self.__textarea.configure(state="normal")
                    self.__textarea.insert("0.0", name + " attendance marked successfully\n")
                    self.__attendancesql.insertAttendance(self.__date, name)
                    self.enrolls.append(name)
                    self.__textarea.configure(state="disabled")
                else:
                    continue
            else:
                self.__textarea.configure(state="normal")
                self.__textarea.insert("0.0", "Unknown face detected\n")
                self.__textarea.configure(state="disabled")

        self.__button.configure(command=self.onClosing)
        self.after(1, self.__recognize)

    def onClosing(self):
        self.__attendanceFirebase.insertAttendance(self.__date, self.enrolls)
        # Release handle to the webcam
        self.__videoCapture.release()
        cv2.destroyAllWindows()
        self.destroy()
