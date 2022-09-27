# Date    : 25/09/22 8:25 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
from PIL import ImageTk, Image


def load_image(frame, path, image_size):
    """
    This function is used to load the image
    :param frame: frame in which the image is to be loaded
    :param path: path of the image
    :param image_size: size of the image
    :return: image
    """
    return ImageTk.PhotoImage(master=frame, image=Image.open(path).resize((image_size, image_size)))
