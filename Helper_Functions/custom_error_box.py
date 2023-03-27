# Date    : 12/08/22 7:27 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
from customtkinter import *
from PIL import ImageTk, Image

import configure
from Helper_Functions.load_image import load_image


class CustomBox(CTkToplevel):
    def error_box(self, title, message):
        self.title(title)
        self.resizable(False, False)
        self.configure(bg=configure.very_dark_gray)
        self.geometry("350x175+{}+{}".format(configure.screen_height / 2, configure.screen_width / 2))
        img = load_image(self, 'Icons/error.png', 35)
        self.iconphoto(False, img)
        error_image = CTkLabel(master=self, image=img, anchor='nw')
        error_image.place(x=10, y=15)
        label = CTkTextbox(master=self, width=300, height=100, state='normal', text_font=configure.welcome_fontstyle,
                           border_color=configure.very_dark_gray, fg_color=configure.very_dark_gray,
                           text_color=configure.white)
        label.place(x=50, y=10)
        label.insert('end', message)
        label.configure(state='disabled')
        button = CTkButton(master=self, text='OK', width=100, height=35, text_font=configure.welcome_fontstyle,
                           fg_color=configure.light_cyan, text_color=configure.very_dark_gray,
                           border_color=configure.white, hover_color=configure.vivid_cyan,
                           command=self.destroy, corner_radius=15)
        button.place(x=125, y=130)
        self.mainloop()