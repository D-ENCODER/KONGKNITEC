import cv2
from pathlib import Path
from PIL import Image, ImageTk
import customtkinter as ctk


# import Helper_Functions.custom_error_box


def generateDataset(userId, userName):
    # Initialize the classifier
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # Start the video camera
    vc = cv2.VideoCapture(0)
    # Get the userId and userName
    # print("Enter the id and name of the person: ")
    # userId = input()
    # userName = input()
    # Initially Count is = 1
    counter = 1

    # Function to save the image
    def save_image(image, username, userid, imgid):
        # Create a folder with the name as userName
        Path("Dataset/{}".format(userid + "_" + username)).mkdir(
            parents=True, exist_ok=True
        )
        # Save the images inside the previously created folder
        cv2.imwrite(
            "Dataset/{}/{}_{}.jpg".format(userid + "_" + username, userid, imgid), image
        )
        print("[INFO] Image {} has been saved in folder : {}".format(imgid, username))

    print("[INFO] Video Capture is now starting please stay still...")
    app1 = ctk.CTk()
    app1.geometry("700x600")
    frame = ctk.CTkLabel(master=app1)
    frame.grid(row=0, column=0)
    progressbar = ctk.CTkProgressBar(master=app1)
    progressbar.grid(row=3, column=0, rowspan=2)

    def set_frame(progress, count):
        # Capture the frame/image
        _, img = vc.read()
        # Copy the original Image
        originalImg = img.copy()
        # Get the gray version of our image
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Get the coordinates of the location of the face in the picture
        faces = faceCascade.detectMultiScale(
            gray_img, scaleFactor=1.3, minNeighbors=5, minSize=(50, 50)
        )
        temp = []
        # Draw a rectangle at the location of the coordinates
        for (x, y, w, h) in faces:
            offset = 10
            face_offset = img[y - offset:y + h + offset, x - offset:x + w + offset]
            # face_selection = cv2.resize(face_offset, (100, 100))
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            temp = [x, y, w, h]
            coords = [x, y, w, h]
        # print(coords)
        if not temp:
            app1.destroy()
            obj = Helper_Functions.custom_error_box.CustomBox()
            obj.errorBox('No Face Detected', 'Please stay in the well lighted room to detect your face')
            return
        image = Image.fromarray(img)
        # converts image frame to tkinter compatible image
        img_frame = ImageTk.PhotoImage(master=app1, image=image)
        frame.img_frame = img_frame
        frame.configure(image=img_frame)
        # to show real time progress
        progress += 4
        progressbar.set(progress / 100)

        def sender():
            set_frame(progress, progress / 4)

        if progress / 4 <= 26:
            roi_img = originalImg[
                      coords[1]: coords[1] + coords[3], coords[0]: coords[0] + coords[2]
                      ]
            save_image(roi_img, userName, userId, count)
        else:
            print("[INFO] Dataset has been created for {}".format(userName))
            vc.release()
            app1.destroy()
            return
        frame.after(20, sender)
        # If q is pressed break out of the loop

    prog = 0
    set_frame(prog, counter)
    app1.mainloop()


generateDataset('3', 'Het')
