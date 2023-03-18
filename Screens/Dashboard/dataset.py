# Date    : 15/02/23 6:51 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
from tkinter import PhotoImage

import customtkinter as ctk
import configure
from Backend.dataset_sqlite_services import DatasetSqliteServices
from Backend.signup_sqlite_services import SignupSqliteServices
from Screens.Dashboard.FaceModules.face_detection import FaceDetection
from Screens.Refactor.customWidgets import CustomWidgets


class Dataset(ctk.CTkFrame):
    def __init__(self, **kwargs):
        ctk.CTkFrame.__init__(self, kwargs['parent'], fg_color=configure.very_dark_gray)
        self.__parent = kwargs['parent']
        self.__controller = kwargs['controller']
        self.sql = DatasetSqliteServices()
        self.signupsql = SignupSqliteServices()
        self.label = ctk.CTkLabel(master=self, text='', text_font=(configure.font, 20))
        self.__datasetGUI()

    def __datasetGUI(self):
        ctk.CTkLabel(master=self, text='', height=15).grid(row=0, column=0)
        self.__option = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        self.__size = (configure.screen_width - (configure.screen_width / 4) - 250)
        ctk.CTkLabel(master=self.__option, text='', width=self.__size).grid(row=0, column=0)
        self.__addDataset = ctk.CTkButton(master=self.__option, text='Add',
                                          text_font=(configure.font, 13, "bold"), command=lambda: self.add(),
                                          text_color=configure.very_dark_gray, fg_color=configure.vivid_cyan,
                                          hover_color=configure.light_cyan, width=100, height=35, corner_radius=10)
        self.__addDataset.grid(row=0, column=1, sticky='e')
        self.__editDataset = ctk.CTkButton(master=self.__option, text='Edit', text_font=(configure.font, 13, "bold"),
                                           text_color=configure.very_dark_gray,
                                           fg_color=configure.vivid_cyan,
                                           hover_color=configure.light_cyan, width=100, height=35, corner_radius=10)
        self.__editDataset.grid(row=0, column=2, padx=25)
        self.__option.grid(row=1, column=0)
        if not self.sql.getDatasetDetails():
            self.__emptyDatasetGUI()
        else:
            self.__tableGUI()

    def add(self):
        window = ctk.CTkToplevel()
        window.geometry('350x150')
        window.title('Add Dataset')
        window.configure(bg=configure.very_dark_gray)
        icon = PhotoImage(file="Assets/logo.png")
        window.iconphoto(False, icon)
        window.focus()
        frame = ctk.CTkFrame(master=window, fg_color=configure.very_dark_gray)
        frame.grid(row=0, column=0)
        entry = CustomWidgets.customEntry(parent=frame, placeholder='Enrollment No')
        entry.grid(row=0, column=0)

        def addDataset(enrollment):
            if not enrollment:
                CustomWidgets.customErrorLabel(parent=frame,
                                               error_text='Empty Enrollment No',).grid(row=1, column=0)
            elif not enrollment.isdigit():
                CustomWidgets.customErrorLabel(parent=frame,
                                               error_text='Enrollment No must be numeric', ).grid(row=1, column=0)
            elif len(enrollment) != 12:
                CustomWidgets.customErrorLabel(parent=frame,
                                               error_text='Enrollment No must be of 12 digits', ).grid(row=1, column=0)
            else:
                name = list(self.signupsql.fetchCondition('Fname, Lname', enrollment)[0])
                name = name[0] + '_' + name[1]
                obj = FaceDetection(master=self, name=name)
                window.destroy()

        button = CustomWidgets.customButton(parent=frame, text='Add Dataset', command=lambda: addDataset(entry.get()))
        button.grid(row=2, column=0)

    def __tableGUI(self):
        pass

    def __emptyDatasetGUI(self):
        frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        frame.grid(row=2, column=0, sticky='nsew', padx=(((configure.screen_width / 4) * 3) - 140) / 2,
                   pady=(configure.screen_height - 191) / 2)
        label = ctk.CTkLabel(frame, text='Dataset is empty!!', text_font=configure.welcome_fontstyle,
                             fg_color=configure.very_dark_gray)
        label.grid(row=1, column=1)
