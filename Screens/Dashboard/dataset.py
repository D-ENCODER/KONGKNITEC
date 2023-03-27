# Date    : 15/02/23 6:51 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import fnmatch
import os
from tkinter import PhotoImage
import customtkinter as ctk
from PIL import Image

import configure
from Backend.SqliteServices.dataset_sqlite_services import DatasetSqliteServices
from Backend.SqliteServices.signup_sqlite_services import SignupSqliteServices
from Screens.Dashboard.FaceModules.data_training import TrainDataset
from Screens.Dashboard.FaceModules.face_detection import FaceDetection
from Screens.Refactor.customWidgets import CustomWidgets


class Dataset(ctk.CTkFrame):
    def __init__(self, **kwargs):
        ctk.CTkFrame.__init__(self, kwargs['parent'], fg_color=configure.very_dark_gray)
        self.__parent = kwargs['parent']
        self.__controller = kwargs['controller']
        self.datasetsql = DatasetSqliteServices()
        self.signupsql = SignupSqliteServices()
        self.__frame = ctk.CTkScrollableFrame(master=self, fg_color=configure.very_dark_gray,
                                              width=(configure.screen_width / 4) * 3,
                                              height=(configure.screen_height - 200))
        self.__frame.grid(row=3, column=0)
        self.__emptyFrame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        self.__emptyFrame.grid(row=2, column=0, sticky='nsew', padx=(((configure.screen_width / 4) * 3) - 140) / 2,
                               pady=(configure.screen_height - 191) / 2)
        self.label = ctk.CTkLabel(master=self, text='', font=(configure.font, 20))
        self.__datasetGUI()

    def __datasetGUI(self):
        ctk.CTkLabel(master=self, text='', height=15).grid(row=0, column=0)
        self.__option = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        self.__size = (configure.screen_width - (configure.screen_width / 4) - 650)
        ctk.CTkLabel(master=self.__option, text='', width=self.__size).grid(row=0, column=0)
        image = ctk.CTkImage(Image.open('Assets/sync.png'), size=(25, 25))
        self.__refreshTable = ctk.CTkButton(master=self.__option, text='', command=lambda: self.refresh(), hover=False,
                                            fg_color=configure.very_dark_gray, image=image, width=35, height=35,
                                            corner_radius=180)
        self.__refreshTable.grid(row=0, column=1, sticky='e')
        self.__addDataset = ctk.CTkButton(master=self.__option, text='Add',
                                          font=(configure.font, 18, "bold"), command=lambda: self.add(),
                                          text_color=configure.very_dark_gray, fg_color=configure.vivid_cyan,
                                          hover_color=configure.light_cyan, width=100, height=35, corner_radius=10)
        self.__addDataset.grid(row=0, column=2, sticky='e', padx=25)
        self.__editDataset = ctk.CTkButton(master=self.__option, text='Edit', font=(configure.font, 18, "bold"),
                                           text_color=configure.very_dark_gray,
                                           fg_color=configure.vivid_cyan, command=lambda: self.edit(),
                                           hover_color=configure.light_cyan, width=100, height=35, corner_radius=10)
        self.__editDataset.grid(row=0, column=3)
        self.trainDataset = ctk.CTkButton(master=self.__option, text='Train', font=(configure.font, 18, "bold"),
                                          text_color=configure.very_dark_gray,
                                          fg_color=configure.vivid_cyan, command=lambda: self.train(),
                                          hover_color=configure.light_cyan, width=100, height=35, corner_radius=10)
        self.trainDataset.grid(row=0, column=4, padx=25)
        self.__option.grid(row=1, column=0)
        fileOfDirectory = os.listdir('Dataset')
        pattern = "*.jpg"
        names = []
        for filename in fileOfDirectory:
            if fnmatch.fnmatch(filename, pattern):
                names.append(filename)
        if not names:
            self.__emptyDatasetGUI()
        else:
            self.__tableGUI()

    def refresh(self):
        fileOfDirectory = os.listdir('Dataset')
        pattern = "*.jpg"
        names = []
        for filename in fileOfDirectory:
            if fnmatch.fnmatch(filename, pattern):
                names.append(filename)
        if not names:
            self.__emptyFrame.destroy()
            self.__emptyDatasetGUI()
        else:
            self.__frame.destroy()
            self.__tableGUI()

    def add(self):
        window = ctk.CTkToplevel()
        window.geometry("400x200+{}+{}".format((configure.screen_width / 2) - 200, (configure.screen_height / 2) - 150))
        window.title('Add Dataset')
        window.configure(bg=configure.very_dark_gray)
        icon = PhotoImage(file="Assets/logo.png")
        window.iconphoto(False, icon)
        window.focus()
        frame = ctk.CTkFrame(master=window, fg_color=configure.very_dark_gray)
        frame.grid(row=0, column=0)
        entry = CustomWidgets.customEntry(parent=frame, placeholder='Enrollment No')
        entry.grid(row=0, column=0, pady=50, padx=55)

        def addDataset(enrollment):
            if not enrollment:
                CustomWidgets.customErrorLabel(parent=frame,
                                               error_text='Empty Enrollment No', ).grid(row=1, column=0)
            elif not enrollment.isdigit():
                CustomWidgets.customErrorLabel(parent=frame,
                                               error_text='Enrollment No must be numeric', ).grid(row=1, column=0)
            elif len(enrollment) != 12:
                CustomWidgets.customErrorLabel(parent=frame,
                                               error_text='Enrollment No must be of 12 digits', ).grid(row=1, column=0)
            else:
                if os.path.isfile('Dataset/' + enrollment + '.jpg'):
                    CustomWidgets.customErrorLabel(parent=frame,
                                                   error_text='Dataset already exists', ).grid(row=1, column=0)
                else:
                    obj = FaceDetection(master=self, enrollment=enrollment)
                    window.destroy()

        button = CustomWidgets.customButton(parent=frame, text='Add Dataset', command=lambda: addDataset(entry.get()))
        button.grid(row=2, column=0)

    def train(self):
        obj = TrainDataset(self.trainDataset)

    def edit(self):
        window = ctk.CTkToplevel()
        window.geometry("400x200+{}+{}".format((configure.screen_width / 2) - 200, (configure.screen_height / 2) - 150))
        window.title('Add Dataset')
        window.configure(bg=configure.very_dark_gray)
        icon = PhotoImage(file="Assets/logo.png")
        window.iconphoto(False, icon)
        window.focus()
        frame = ctk.CTkFrame(master=window, fg_color=configure.very_dark_gray)
        frame.grid(row=0, column=0)
        enrolls = list(self.datasetsql.getId())
        temp = []
        for i in enrolls:
            temp.append(str(i[0]))
        enrolls = temp
        id = ctk.CTkComboBox(master=frame, width=250, corner_radius=10, values=enrolls)
        id.grid(row=0, column=0, pady=50, padx=55)

        def editDataset():
            enroll = list(self.datasetsql.getEnrollment(id.get())[0])
            enroll = enroll[0]
            window.destroy()
            obj = FaceDetection(master=self, enrollment=enroll)

        button = CustomWidgets.customButton(parent=frame, text='Edit', command=lambda: editDataset())
        button.grid(row=2, column=0)

    def __tableGUI(self):
        self.__emptyFrame.destroy()
        Directoryfile = os.listdir('Dataset')
        pattern = "*.jpg"
        enroll = []
        for filename in Directoryfile:
            if fnmatch.fnmatch(filename, pattern):
                enroll.append(filename.split('.')[0])
        self.datasetsql.massInsert(enroll)
        data = list(self.datasetsql.getDatasetDetails())
        ctk.CTkLabel(master=self, text='').grid(row=2, column=0)
        self.__frame = ctk.CTkScrollableFrame(master=self, fg_color=configure.very_dark_gray,
                                              width=(configure.screen_width / 4) * 3,
                                              height=(configure.screen_height - 200))
        self.__frame.grid(row=3, column=0)
        table_header = ['SR No.', 'Enrollment No.', 'Name', 'E-mail', 'Date']
        for i in range(len(table_header)):
            self.label = ctk.CTkLabel(master=self.__frame, text=table_header[i], font=(configure.font, 23, "bold"),
                                      text_color=configure.vivid_cyan)
            self.label.grid(row=0, column=i, sticky='nsew', padx=20)
        for details in range(len(data)):
            for fields in range(len(data[details])):
                self.label = ctk.CTkLabel(master=self.__frame, text=data[details][fields], font=(configure.font, 20))
                self.label.grid(row=details + 1, column=fields, sticky='nsew', padx=20, pady=10)

    def __emptyDatasetGUI(self):
        self.__frame.destroy()
        self.__emptyFrame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        self.__emptyFrame.grid(row=2, column=0, sticky='nsew', padx=(((configure.screen_width / 4) * 3) - 140) / 2,
                               pady=(configure.screen_height - 191) / 2)
        label = ctk.CTkLabel(self.__emptyFrame, text='No Data available!!', font=configure.welcome_fontstyle,
                             fg_color=configure.very_dark_gray)
        label.grid(row=1, column=1)
