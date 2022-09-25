# Date    : 24/09/22 10:06 am
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import customtkinter as ctk
import configure
from Helper_Functions.load_image import load_image


def footer_gui(self, label, controller, hyper_label, frame):
    """
    This function is used to create footer for the given frame
    :param self: object of the class
    :param label: label to be displayed
    :param controller: controller of the frame
    :param hyper_label: label to be displayed as hyperlink
    :param frame: frame to which footer is to be added
    :return: None
    """
    # Create a frame for footer
    self._login_frame = ctk.CTkFrame(master=self, fg_color=configure.hyperlink_color, corner_radius=180)
    # load all the images used in the frame for footer
    self._google_icon = load_image(self._login_frame, "Icons/google.png", 27)
    self._git_icon = load_image(self._login_frame, "Icons/git.png", 27)
    self._twitter_icon = load_image(self._login_frame, "Icons/twitter.png", 27)
    # Create a label for footer
    ctk.CTkLabel(master=self, text=label,
                 text_font=(configure.font, 9), text_color=configure.non_dominant_color).grid(row=8, column=0,
                                                                                              sticky='e')
    # Create a hyperlink label for footer
    ctk.CTkButton(master=self, text=hyper_label, width=70, height=35, text_font=(configure.font, 10,
                                                                                 "bold"),
                  cursor="hand2", fg_color=configure.hover_color, hover=False,
                  command=lambda: controller.show_frame(frame),
                  text_color=configure.dominant_color).grid(row=8, column=1, sticky='w')
    # Create a frame for footer
    ctk.CTkLabel(master=self, text='--OR--',
                 text_font=(configure.font, 9, "bold"), text_color=configure.dominant_color).grid(row=9, column=0,
                                                                                                  columnspan=2)

    def caller():
        pass

    # Create third party authentication buttons frame for footer
    ctk.CTkButton(master=self._login_frame, image=self._google_icon, text="", width=30, hover=False, cursor='hand2',
                  fg_color=configure.hyperlink_color, command=caller, ).grid(row=0, column=0, padx=7, pady=10)

    ctk.CTkButton(master=self._login_frame, image=self._git_icon, text="", width=30, hover=False, cursor='hand2',
                  fg_color=configure.hyperlink_color, command=caller).grid(row=0, column=1, padx=50, pady=10)

    ctk.CTkButton(master=self._login_frame, image=self._twitter_icon, text="", width=30, hover=False,
                  cursor='hand2', fg_color=configure.hyperlink_color, command=caller).grid(row=0, column=2,
                                                                                           padx=7, pady=10)
    # Place the frame for footer
    self._login_frame.grid(row=10, column=0, columnspan=2)
