# Date    : 15/02/23 6:52 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import customtkinter as ctk
import configure
from Backend.sqlite_services import SqliteServices


class Attendance(ctk.CTkFrame):
    def __init__(self, **kwargs):
        ctk.CTkFrame.__init__(self, kwargs['parent'], fg_color=configure.very_dark_gray)
        self.__parent = kwargs['parent']
        self.__controller = kwargs['controller']
        self.sql = SqliteServices()
        self.__attendanceGUI()

    def __attendanceGUI(self):
        ctk.CTkLabel(master=self, text='', height=15).grid(row=0, column=0)
        self.__option = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        self.__size = (configure.screen_width - (configure.screen_width / 4) - 220)
        ctk.CTkLabel(master=self.__option, text='', width=self.__size).grid(row=0, column=0)
        self.__takeAttendance = ctk.CTkButton(master=self.__option, text='Take',
                                              text_font=(configure.font, 13, "bold"),
                                              text_color=configure.very_dark_gray, fg_color=configure.vivid_cyan,
                                              hover_color=configure.light_cyan, width=100, height=35, corner_radius=10)
        self.__takeAttendance.grid(row=0, column=1, sticky='e')
        ctk.CTkLabel(master=self.__option, text='', width=20).grid(row=0, column=2)
        self.__addAttendance = ctk.CTkButton(master=self.__option, text='Add', text_font=(configure.font, 13, "bold"),
                                             text_color=configure.very_dark_gray, fg_color=configure.vivid_cyan,
                                             hover_color=configure.light_cyan, width=100, height=35, corner_radius=10)
        self.__addAttendance.grid(row=0, column=3)
        self.__option.grid(row=1, column=0)
