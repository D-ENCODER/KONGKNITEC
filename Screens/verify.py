# Date    : 28/09/22 10:47 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import customtkinter as ctk
import configure
from Screens.Refactor.custom_widgets import CustomWidgets
from Screens.Refactor.header_gui import header_gui
from Screens.forgot_password import ForgotPassword


class Verify(ForgotPassword):
    def __init__(self, **kwargs):
        ctk.CTkFrame.__init__(self, kwargs['parent'], fg_color=configure.hover_color)
        self._controller = kwargs['controller']
        self._verifyGUI()

    def _verifyGUI(self):
        header_gui(self)
        CustomWidgets.customHeaderLabel(self, 'Verify').grid(row=3, column=0)
        self.otp_frame = ctk.CTkFrame(master=self, fg_color=configure.hover_color)
        self.otp_entry = CustomWidgets.customEntry(self.otp_frame, 'Enter OTP')
        self.otp_entry.grid(row=0, column=0, columnspan=2)
        self.otp_frame.grid(row=4, column=0, columnspan=2, pady=10)

        def verify():
            if self.otp == self.otp_entry.get():
                print('success 200')
            else:
                print('failed 400')

        CustomWidgets.customButton(self, 'VERIFY', verify).grid(row=5, column=0, columnspan=2, pady=10)
