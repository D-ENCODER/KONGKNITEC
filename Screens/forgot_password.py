# Date    : 28/09/22 8:53 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import customtkinter as ctk
import configure
from Helper_Functions.custom_error_box import CustomBox
from Helper_Functions.otp_sender import sendOtp
from Screens.Refactor.custom_widgets import CustomWidgets
from Screens.Refactor.header_gui import header_gui
from Screens.Validator.validator import validate_email


class ForgotPassword(ctk.CTkFrame):
    """
    Frame to show the forgot password screen
    """
    otp = None
    email = None

    def __init__(self, **kwargs):
        """
        constructor of the class to initialize the frame
        """
        super().__init__(kwargs['parent'], fg_color=configure.very_dark_gray)
        self._controller = kwargs['controller']
        self.email_error_label = ctk.CTkLabel()
        self._forgotPasswordGUI()

    def _forgotPasswordGUI(self):
        header_gui(self)
        CustomWidgets.customHeaderLabel(self, 'RECOVERY').grid(row=3, column=0, sticky='w')
        self.email_frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        self.email_entry = CustomWidgets.customEntry(parent=self.email_frame, placeholder='E-mail address')
        self.email_entry.grid(row=0, column=0, columnspan=2)
        self.email_frame.grid(row=4, column=0, columnspan=2, pady=10)
        self.email_entry.bind('<FocusOut>', lambda event: validate_email(parent=self))

        def validate():
            if validate_email(parent=self):
                try:
                    ForgotPassword.otp = sendOtp(self.email_entry.get())
                    ForgotPassword.email = self.email_entry.get()
                    self._controller.show_frame('Verify')
                except Exception as e:
                    obj = CustomBox()
                    obj.error_box('Error', 'Something went wrong' + '(' + str(e.args[0]) + ')')
            else:
                validate_email(parent=self)

        CustomWidgets.customButton(self=self, text='BACK', command=lambda: self._controller.show_frame('Login'),
                                   fg_color=configure.dark_gray, text_color=configure.white,
                                   hover_color=configure.very_dark_gray).grid(row=5, column=0, pady=10)
        CustomWidgets.customButton(self=self, text='SEND', command=validate).grid(row=5, column=1, pady=10)
