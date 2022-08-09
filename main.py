# Date    : 20/07/22 10:01 PM
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0

import math
import random
import smtplib
import customtkinter as ctk
from Facial_Recognition import generate_dataset, recognize, train_model

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.geometry("400x240")
app.title('Attendance With Face Recognition')


def generate():
    app1 = ctk.CTk()
    app1.title('Generate Dataset')
    app1.geometry("400x240")
    user_id_text = ctk.CTkLabel(master=app1, text='Enrollment No')
    user_id_text.grid(row=1, column=0)
    user_id = ctk.CTkEntry(master=app1, placeholder_text='Enter your Id')
    user_id.grid(row=1, column=2, columnspan=2, pady=20, padx=20, sticky="we")
    # user_id.place()
    name_text = ctk.CTkLabel(master=app1, text='Name')
    name_text.grid(row=2, column=0)
    name = ctk.CTkEntry(master=app1, placeholder_text='Enter your Name')
    name.grid(row=2, column=2, columnspan=2, pady=20, padx=20, sticky="we")

    # name.place()
    def submit():
        generate_dataset.generateDataset(user_id.get(), name.get())

    submit = ctk.CTkButton(master=app1, text='Submit', command=submit)
    submit.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)
    app.mainloop()


user_email = ctk.CTkLabel(master=app, text="Email")
user_email.grid(row=1, column=0)
email = ctk.CTkEntry(master=app, placeholder_text='Enter Email')
email.grid(row=1, column=2, columnspan=2, pady=20, padx=20)
# user_id.place()
user_password = ctk.CTkLabel(master=app, text='Password')
user_password.grid(row=2, column=0)
password = ctk.CTkEntry(master=app, placeholder_text='Enter Password')
password.grid(row=2, column=2, columnspan=2, pady=20, padx=20)
confirm_password = ctk.CTkLabel(master=app, text='Confirm Password')
confirm_password.grid(row=3, column=0)
con_password = ctk.CTkEntry(master=app, placeholder_text='Renter Password')
con_password.grid(row=3, column=2, columnspan=2, pady=20, padx=20)


def sendOtp(emailid):
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    message = OTP + " use this otp to login"
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login("facioaide2022@gmail.com", "zajtyiewzpnokcrd")
    s.sendmail("&&&&&&", emailid, message)
    return OTP


def sendCredentials():
    emailid = email.get()
    if password.get() == con_password.get():
        user_email.destroy()
        email.destroy()
        user_password.destroy()
        password.destroy()
        confirm_password.destroy()
        con_password.destroy()
        submit_button.destroy()
        otps = sendOtp(emailid)
        user_otp = ctk.CTkLabel(master=app, text="OTP")
        user_otp.grid(row=1, column=0)
        otp = ctk.CTkEntry(master=app, placeholder_text='Enter OTP')
        otp.grid(row=1, column=2, columnspan=2, pady=20, padx=20)

        def verifyCredentials():
            if otps == otp.get():
                user_otp.destroy()
                otp.destroy()
                verify.destroy()
                button = ctk.CTkButton(master=app, text="Generate Dataset", command=generate)
                button.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)
                button1 = ctk.CTkButton(master=app, text="Train Model", command=train_model.trainModel)
                button1.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
                button2 = ctk.CTkButton(master=app, text="Face Recognition", command=recognize.recognize)
                button2.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)

        verify = ctk.CTkButton(master=app, text='Verify', command=verifyCredentials)
        verify.grid(row=4, column=1, columnspan=2)


submit_button = ctk.CTkButton(master=app, text='Submit', command=sendCredentials)
submit_button.grid(row=4, column=1, columnspan=2)


app.mainloop()
