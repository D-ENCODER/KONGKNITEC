# Date    : 12/08/22 7:27 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
from customtkinter import *
from PIL import ImageTk, Image


class CustomBox(CTk):
    def error_box(self, title, message):
        self.title(title)
        self.resizable(False, False)
        self.geometry("330x100")
        image = Image.open('Icons/error.png')
        resized_img = image.resize((75, 75), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(master=self, image=resized_img)
        error_image = CTkLabel(master=self, image=img, anchor='w')
        error_image.grid(row=0, column=0, padx=10)
        label = CTkLabel(master=self, text=message, anchor='w', justify='left', wraplength=75)
        label.grid(row=0, column=1)
        self.mainloop()
