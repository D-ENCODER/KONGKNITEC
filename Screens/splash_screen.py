# Date    : 18/11/22 5:47 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0

from Helper_Functions.video_player import VideoPlayer
import customtkinter as ctk
import configure


class SplashScreen(ctk.CTkFrame):
    def __init__(self, **kwargs):
        ctk.CTkFrame.__init__(self, kwargs['parent'], fg_color=configure.very_dark_gray)
        self._controller = kwargs['controller']
        self._parent = kwargs['parent']
        self._parent.grid_configure(padx=0, pady=0)
        self._splashGUI()

    def _splashGUI(self):
        splash = ctk.CTkLabel(self, text='', height=configure.screen_height, width=configure.screen_width,
                              bg=configure.very_dark_gray, anchor='center')
        splash.grid(row=0, column=0, padx=0, pady=0, columnspan=2)
        splashscreen = VideoPlayer("Icons/splash.mp4", splash, size=(configure.screen_width, configure.screen_height),
                                   controller=self._controller, parent=self._parent)
        splashscreen.play()

