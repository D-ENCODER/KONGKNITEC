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
        defaultKwargs = {'width': 290, 'height': 35, 'font_size': 17, 'obfuscated': False, 'font_weight': 'normal',
                         'border_color': configure.dark_gray}
        kwargs = {**defaultKwargs, **kwargs}
        custom_entry = ctk.CTkEntry(master=kwargs['parent'], placeholder_text=kwargs['placeholder'],
                                    fg_color=configure.dark_gray, border_color=kwargs['border_color'],
                                    border_width=1.5, corner_radius=10, font=(configure.font, kwargs['font_size'],
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
        custom_label = ctk.CTkLabel(master=self, text=text, font=configure.header_fontstyle,
                                    anchor='w', text_color=configure.light_cyan)
        return custom_label

    @staticmethod
    def customButton(**kwargs):
        """
        This method is used to create a custom button widget.
        :return: The custom button widget.
        """
        defaultKwargs = {'hover_color': configure.vivid_cyan, 'fg_color': configure.light_cyan, 'command': None,
                         'text_color': configure.very_dark_gray}
        kwargs = {**defaultKwargs, **kwargs}
        custom_button = ctk.CTkButton(master=kwargs['parent'], text=kwargs['text'], width=100, height=35,
                                      fg_color=kwargs['fg_color'], hover_color=kwargs['hover_color'],
                                      font=(configure.font, 17, "bold"), corner_radius=15,
                                      text_color=kwargs['text_color'],
                                      command=kwargs['command'])
        return custom_button

    @staticmethod
    def customErrorLabel(**kwargs):
        """
        This method is used to create a custom error label widget.
        :param kwargs: The keyword arguments to be passed to the label.
        :return: The custom error label widget.
        """
        defaultKwargs = {'color': configure.light_cyan, 'anchor': 'center'}
        kwargs = {**defaultKwargs, **kwargs}
        custom_error_label = ctk.CTkLabel(master=kwargs['parent'], text=kwargs['error_text'],
                                          font=(configure.font, 13, "bold"),
                                          text_color=kwargs['color'], bg_color=configure.very_dark_gray,
                                          anchor=kwargs['anchor'])
        return custom_error_label

    @staticmethod
    def customHyperlinkLabel(**kwargs):
        """
        This method is used to create a custom hyperlink label widget.
        :param kwargs: The keyword arguments to be passed to the label.
        :return: The custom hyperlink label widget.
        """
        defaultKwargs = {'color': configure.dark_gray, 'anchor': 'center'}
        kwargs = {**defaultKwargs, **kwargs}
        custom_hyperlink_label = ctk.CTkButton(master=kwargs['parent'], text=kwargs['text'], cursor="hand2",
                                               fg_color=configure.very_dark_gray,
                                               font=(configure.font, 17, "bold"),
                                               hover_color=configure.very_dark_gray,
                                               command=kwargs['command'],
                                               text_color=configure.light_cyan)
        return custom_hyperlink_label

    @staticmethod
    def customDashboardButtons(parent, text, image, command):
        """
        Left side panel buttons of dashboard screen
        :param parent: Parent of the button GUI
        :param text: The text to be printed on button
        :param image: Image object to be printed on the button
        :param command: The function to be called whenever the button is pressed or the action event is called
        :return: The custom button widget
        """
        custom_dashboard_button = ctk.CTkButton(master=parent, text=text,
                                                image=image, corner_radius=20,
                                                hover_color=configure.dark_gray,
                                                fg_color=configure.very_dark_gray, width=configure.screen_width / 4,
                                                height=50, command=command,
                                                font=(configure.font, 22, 'bold'), text_color=configure.white)

        return custom_dashboard_button
