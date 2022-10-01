# Date    : 01/10/22 01:00 pm
# Author  : Maulik (mm.2004.parmar@gmail.com)
# GitHub    : (https://github.com/Maulikatgit)
# Twitter    : (https://twitter.com/Mr_younglord)
# Version : 1.0.0
import customtkinter as ctk
import configure
from Screens.Refactor.custom_widgets import CustomWidgets
from Screens.Refactor.header_gui import header_gui


class PersonalInfo(ctk.CTkFrame):
    def __init__(self, **kwargs):
        ctk.CTkFrame.__init__(self, kwargs['parent'], fg_color=configure.hover_color)
        self._controller = kwargs['controller']
        self._personalinfoGUI()

    def _personalinfoGUI(self):
        header_gui(self)
        radio = ctk.IntVar()
        CustomWidgets.customHeaderLabel(self, 'Personal Info').grid(row=3, column=0)
        self.firstname_frame = ctk.CTkFrame(master=self, fg_color=configure.hover_color)
        self.firstname_entry = CustomWidgets.customEntry(parent=self.firstname_frame, placeholder='First name')
        self.firstname_entry.grid(row=0, column=0, columnspan=2)
        self.firstname_frame.grid(row=4, column=0, columnspan=2, pady=10)
        self.lastname_frame = ctk.CTkFrame(master=self, fg_color=configure.hover_color)
        self.lastname_entry = CustomWidgets.customEntry(parent=self.lastname_frame, placeholder='Last name')
        self.lastname_entry.grid(row=0, column=0, columnspan=2)
        self.lastname_frame.grid(row=5, column=0, columnspan=2, pady=10)
        self.birth_frame = ctk.CTkFrame(master=self, fg_color=configure.hover_color)
        self.birth_entry = CustomWidgets.customEntry(parent=self.birth_frame, placeholder='DD/MM/YYYY')
        self.birth_entry.grid(row=0, column=0, columnspan=2)
        self.birth_frame.grid(row=6, column=0, columnspan=2, pady=10)
        ctk.CTkLabel(master=self, text='Gender:', text_color=configure.non_dominant_color,
                     text_font=(configure.font, 11, 'bold'), anchor='w').grid(row=7, column=0, columnspan=2, sticky='w')
        ctk.CTkRadioButton(master=self, text='Male', value=1, variable=radio).grid(row=8, column=0, sticky='w')
        ctk.CTkRadioButton(master=self, text='Female', value=2, variable=radio).grid(row=8, column=0, sticky='e')
        ctk.CTkRadioButton(master=self, text='Not to say', value=3, variable=radio).grid(row=8, column=1, sticky='e')
        ctk.CTkLabel(master=self, text='', anchor='center').grid(row=9, column=0, columnspan=2)

        CustomWidgets.customButton(self, 'Next').grid(row=10, column=0, columnspan=2)
