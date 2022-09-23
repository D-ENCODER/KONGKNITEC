# Date    : 26/08/22 6:55 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0

import customtkinter as ctk

import configure
from Helper_Functions import otp_sender, custom_error_box
from Facial_Recognition import generate_dataset, recognize, train_model


class Signup(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent, fg_color=configure.hover_color)

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

            def submit():
                generate_dataset.generateDataset(user_id.get(), name.get())

            submit = ctk.CTkButton(master=app1, text='Submit', command=submit)
            submit.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)
            app1.mainloop()

        user_email = ctk.CTkLabel(master=self, text="Email")
        user_email.grid(row=1, column=0)
        email = ctk.CTkEntry(master=self, placeholder_text='Enter Email')
        email.grid(row=1, column=2, columnspan=2, pady=20, padx=20)
        user_password = ctk.CTkLabel(master=self, text='Password')
        user_password.grid(row=2, column=0)
        password = ctk.CTkEntry(master=self, placeholder_text='Enter Password')
        password.grid(row=2, column=2, columnspan=2, pady=20, padx=20)
        confirm_password = ctk.CTkLabel(master=self, text='Confirm Password')
        confirm_password.grid(row=3, column=0)
        con_password = ctk.CTkEntry(master=self, placeholder_text='Renter Password')
        con_password.grid(row=3, column=2, columnspan=2, pady=20, padx=20)

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
                # otps = otp_sender.sendOtp(emailid)
                otps = 1234
                user_otp = ctk.CTkLabel(master=self, text="OTP")
                user_otp.grid(row=1, column=0)
                otp = ctk.CTkEntry(master=self, placeholder_text='Enter OTP')
                otp.grid(row=1, column=2, columnspan=2, pady=20, padx=20)

                def verifyCredentials():
                    if otps != otp.get():
                        user_otp.destroy()
                        otp.destroy()
                        verify.destroy()
                        button = ctk.CTkButton(master=self, text="Generate Dataset", command=generate)
                        button.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)
                        button1 = ctk.CTkButton(master=self, text="Train Model", command=train_model.trainModel)
                        button1.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
                        button2 = ctk.CTkButton(master=self, text="Face Recognition", command=recognize.recognize)
                        button2.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)
                    else:
                        otp_error = custom_error_box.CustomBox()
                        otp_error.error_box('ERROR', 'Invalid OTP Please try again')

                verify = ctk.CTkButton(master=self, text='Verify', command=verifyCredentials)
                verify.grid(row=4, column=1, columnspan=2)
            else:
                password_error = custom_error_box.CustomBox()
                password_error.error_box('ERROR', 'Passwords Don\'t match')

        submit_button = ctk.CTkButton(master=self, text='Submit', command=lambda: controller.show_frame('Login'))
        submit_button.grid(row=4, column=1, columnspan=2)

    def on_closing(self):
        self.destroy()
