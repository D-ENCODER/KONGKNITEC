import cv2
import os
import customtkinter as ctk
from PIL import Image, ImageTk
import Helper_Functions.most_frequent
from gtts import gTTS


def recognize():
    """
    Face Recognition Model
    """
    faceCascade = cv2.CascadeClassifier("Classifiers/haarcascade_frontalface_alt.xml")
    # video_capture = cv2.VideoCapture(0)

    # Call the trained model yml file to recognize faces
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("training.yml")

    # Names corresponding to each user_id
    names = []
    for users in os.listdir("Facial_Recognition/Dataset"):
        names.append(users)

    names = sorted(names, key=lambda x: int(x.split("_")[0]))
    print(names)
    # img = cv2.imread("test/robert.jpeg")
    cap = cv2.VideoCapture(0)
    name = []
    app1 = ctk.CTk()
    app1.geometry("700x600")
    frame = ctk.CTkLabel(master=app1)
    frame.grid(row=0, column=0)
    progressbar = ctk.CTkProgressBar(master=app1)
    progressbar.grid(row=3, column=0, rowspan=2)

    def show_frame(progress):
        _, img = cap.read()
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=5)
        # Try to predict the face and get the user_id
        # Then check if user_id == 1 or user_id == 2
        # Accordingly add the names
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            user_id, confidence = recognizer.predict(gray_image[y: y + h, x: x + w])
            if confidence < 100:
                text = names[user_id - 1]
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                text = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))
            name.append(text)
            cv2.putText(
                img,
                str(text),
                (x + 5, y - 5),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                2
            )
            cv2.putText(
                img,
                str(confidence),
                (x + 5, y + h - 5),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 0),
                1
            )
        # creates an image from numpy array
        image = Image.fromarray(img)
        # converts image frame to tkinter compatible image
        img_frame = ImageTk.PhotoImage(master=app1, image=image)
        frame.img_frame = img_frame
        frame.configure(image=img_frame)
        # to show real time progress
        progress += 1
        progressbar.set(progress / 100)

        def send():
            show_frame(progress)

        if progress == 100:
            cap.release()
            app1.destroy()
            voice_obj = gTTS(text='Welcome' + Helper_Functions.most_frequent.most_frequent(name), lang='en', slow=False)
            voice_obj.save("greetings.mp3")
            os.system("start greetings.mp3")
            return
        frame.after(20, send)

    prog = 0
    show_frame(prog)
    app1.mainloop()
