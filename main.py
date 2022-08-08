# Date    : 20/07/22 10:01 PM
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0

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


button = ctk.CTkButton(master=app, text="Generate Dataset", command=generate)
button.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)
button1 = ctk.CTkButton(master=app, text="Train Model", command=train_model.trainModel)
button1.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
button2 = ctk.CTkButton(master=app, text="Face Recognition", command=recognize.recognize)
button2.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)

app.mainloop()
