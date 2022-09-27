# Date    : 24/09/22 10:41 am
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import customtkinter as ctk
import configure


class CustomWidgets:
    """
    This class contains all the custom widgets used in the application
    these widgets are used to make the application look more attractive.
    """

    @staticmethod
    def customEntry(self, placeholder, obfuscated=False):
        """
        This method is used to create a custom entry widget.
        :param self: The object of the class in which this method is called.
        :param placeholder: The placeholder text for the entry widget.
        :param obfuscated: If True, the text in the entry widget will be obfuscated.
        :return: The custom entry widget.
        """
        custom_entry = ctk.CTkEntry(master=self, placeholder_text=placeholder,
                                    fg_color=configure.hyperlink_color, border_color=configure.hyperlink_color,
                                    border_width=1.5, corner_radius=10, text_font=(configure.font, 10), width=290,
                                    height=35, show='•' if obfuscated else '')
        return custom_entry

    @staticmethod
    def customHeaderLabel(self, text):
        """
        This method is used to create a custom header label widget.
        like LOGIN and SIGNUP.
        :param self: The object of the class in which this method is called.
        :param text: The text to be displayed in the header label.
        :return: The header label widget.
        """
        custom_label = ctk.CTkLabel(master=self, text=text, text_font=(configure.font, 18, "bold"),
                                    anchor='w', text_color=configure.dominant_color)
        return custom_label

    @staticmethod
    def customButton(self, text, command=None):
        """
        This method is used to create a custom button widget.
        :param self: The object of the class in which this method is called.
        :param text: The text to be displayed on the button.
        :param command: The command to be executed when the button is clicked.
        :return: The custom button widget.
        """
        custom_button = ctk.CTkButton(master=self, text=text, width=100, height=35,
                                      fg_color=configure.dominant_color,
                                      text_font=(configure.font, 10, "bold"), hover=False, corner_radius=15,
                                      text_color=configure.hover_color,
                                      command=command)
        return custom_button

    @staticmethod
    def customErrorLabel(self, error_text):
        """
        This method is used to create a custom error label widget.
        :param self: The object of the class in which this method is called.
        :param error_text: The text to be displayed in the error label.
        :return: The custom error label widget.
        """
        custom_error_label = ctk.CTkLabel(master=self, text=error_text, text_font=(configure.font, 8, "bold"),
                                          text_color=configure.dominant_color, bg_color=configure.hover_color)
        return custom_error_label
