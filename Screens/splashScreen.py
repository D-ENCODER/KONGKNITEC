# Date    : 18/11/22 5:47 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0

from Helper_Functions.videoPlayer import VideoPlayer
import customtkinter as ctk
import configure
import os


class SplashScreen(ctk.CTkFrame):
    def __init__(self, **kwargs):
        ctk.CTkFrame.__init__(self, kwargs['parent'], fg_color=configure.very_dark_gray)
        self._controller = kwargs['controller']
        self._parent = kwargs['parent']
        self._parent.grid_configure(padx=0, pady=0)
        self._splashGUI()

    def _splashGUI(self):
        splash = ctk.CTkLabel(self, text='', height=350, width=600,
                              bg=configure.very_dark_gray, anchor='center')
        splash.pack(padx=((configure.screen_width-600)/2), pady=((configure.screen_height-350)/2))
        splashscreen = VideoPlayer("Assets/splash.gif", splash,
                                   controller=self._controller, parent=self._parent)
        splashscreen.play()

