# Date    : 28/09/22 9:06 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
from numpy.core.defchararray import strip
import configure
from Screens.Refactor.custom_widgets import CustomWidgets
from Screens.Validator.validator_logic import Validator


# This function is used to validate the email address when the focus pops out of the entry
def validate_fields(**kwargs):
    """
    This function is used to validate the fields when the focus pops out of the entry
    :return: None
    """
    if strip(kwargs['widget'].get()) != "":
        kwargs['error_widget'].destroy()
        # reset the color of the entry to default
        kwargs['widget'].configure(border_color=configure.dark_gray)
        kwargs['bool'] = True
        return kwargs['bool']
    else:
        # Place the error label in the grid layout
        kwargs['error_widget'].grid(row=1, column=0, columnspan=2)
        kwargs['widget'].configure(border_color=configure.light_cyan)
        kwargs['bool'] = False
        return kwargs['bool']


def validate_email(**kwargs):
    """
    This is the function which is used to validate the email address when the focus pops out of the entry
    :return: None
    """
    if Validator.validate_email(kwargs['parent'].email_entry.get())[0]:
        # If the email is valid then remove the error label
        kwargs['parent'].email_error_label.destroy()
        # reset the color of the entry to default
        kwargs['parent'].email_entry.configure(border_color=configure.dark_gray)
        return True
    else:
        # checks if the error label is already present or not
        if kwargs['parent'].email_error_label.winfo_exists():
            # If the error label is already present then destroy it
            kwargs['parent'].email_error_label.destroy()
        # Create the custom error label
        kwargs['parent'].email_error_label = CustomWidgets.customErrorLabel(self=kwargs['parent'].email_frame,
                                                                            error_text=Validator.validate_email(
                                                                                kwargs['parent'].email_entry.get())[1])
        # Place the error label in the grid layout
        kwargs['parent'].email_error_label.grid(row=1, column=0, columnspan=2)
        # Change the color of the entry to dominant color
        kwargs['parent'].email_entry.configure(border_color=configure.light_cyan)
        return False


def validate_password(**kwargs):
    """
    This is the function which is used to validate the password when the focus pops out of the entry
    :return: None
    """
    if Validator.validate_password(kwargs['parent'].password_entry.get())[0]:
        # If the password is valid then remove the error label
        kwargs['parent'].password_error_label.destroy()
        # reset the color of the entry to default
        kwargs['parent'].password_entry.configure(border_color=configure.dark_gray)
        return True
    else:
        # checks if the error label is already present or not
        if kwargs['parent'].password_error_label.winfo_exists():
            # If the error label is already present then destroy it
            kwargs['parent'].password_error_label.destroy()
        # Create the custom error label
        kwargs['parent'].password_error_label = CustomWidgets.customErrorLabel(self=kwargs['parent'].password_frame,
                                                                               error_text=Validator.validate_password(
                                                                                   kwargs[
                                                                                       'parent'].password_entry.get())[
                                                                                   1])
        # Place the error label in the grid layout
        kwargs['parent'].password_error_label.grid(row=1, column=0, columnspan=2)
        # Change the color of the entry to dominant color
        kwargs['parent'].password_entry.configure(border_color=configure.light_cyan)
        return False
