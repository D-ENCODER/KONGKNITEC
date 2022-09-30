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
    def customEntry(**kwargs):
        """
        This method is used to create a custom entry widget.
        :param kwargs: This is a dictionary of all the parameters required to create a custom entry widget.
        :return: The custom entry widget.
        """
        defaultKwargs = {'width': 290, 'height': 35, 'font_size': 10, 'obfuscated': False, 'font_weight': 'normal',
                         'border_color': configure.hyperlink_color}
        kwargs = {**defaultKwargs, **kwargs}
        custom_entry = ctk.CTkEntry(master=kwargs['parent'], placeholder_text=kwargs['placeholder'],
                                    fg_color=configure.hyperlink_color, border_color=kwargs['border_color'],
                                    border_width=1.5, corner_radius=10, text_font=(configure.font, kwargs['font_size'],
                                                                                   kwargs['font_weight']),
                                    width=kwargs['width'],
                                    height=kwargs['height'], show='•' if kwargs['obfuscated'] else '')
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
    def customErrorLabel(**kwargs):
        """
        This method is used to create a custom error label widget.
        :param kwargs: The keyword arguments to be passed to the label.
        :return: The custom error label widget.
        """
        defaultKwargs = {'color': configure.dominant_color, 'anchor': 'center'}
        kwargs = {**defaultKwargs, **kwargs}
        custom_error_label = ctk.CTkLabel(master=kwargs['self'], text=kwargs['error_text'],
                                          text_font=(configure.font, 8, "bold"),
                                          text_color=kwargs['color'], bg_color=configure.hover_color,
                                          anchor=kwargs['anchor'])
        return custom_error_label

    @staticmethod
    def customHyperlinkLabel(**kwargs):
        """
        This method is used to create a custom hyperlink label widget.
        :param kwargs: The keyword arguments to be passed to the label.
        :return: The custom hyperlink label widget.
        """
        defaultKwargs = {'color': configure.hyperlink_color, 'anchor': 'center'}
        kwargs = {**defaultKwargs, **kwargs}
        custom_hyperlink_label = ctk.CTkButton(master=kwargs['self'], text=kwargs['text'], cursor="hand2",
                                               fg_color=configure.hover_color, text_font=(configure.font, 8, "bold"),
                                               hover_color=configure.hover_color,
                                               command=kwargs['command'],
                                               text_color=configure.dominant_color)
        return custom_hyperlink_label
