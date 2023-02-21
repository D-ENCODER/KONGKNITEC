# Date    : 21/02/23 08:00 pm
# Author  : Parmar Maulik (mm.2004.parmar@gmail.com)
# GitHub    : (https://github.com/Maulikatgit)
# Twitter    : (https://twitter.com/Mr_younglord)
# Version : 1.0.0
import customtkinter as ctk
from PIL.ImageTk import PhotoImage
import configure
from Backend.sqlite_services import SqliteServices


class Take(ctk.CTkFrame):
    def __init__(self, **kwargs):
        ctk.CTkFrame.__init__(self, kwargs['parent'], fg_color=configure.very_dark_gray)
        self.__parent = kwargs['parent']
        self.__controller = kwargs['controller']
        self.sql = SqliteServices()
        self.__takeGUI()

    def __takeGUI(self):
        pass
