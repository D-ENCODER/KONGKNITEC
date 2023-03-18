# Date    : 20/11/22 12:27 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import threading
from time import sleep

import imageio
from PIL import Image, ImageTk

import configure
from Backend.signup_sqlite_services import SignupSqliteServices


class VideoPlayer:
    """
        Main class of tkVideo. Handles loading and playing
        the video inside the selected label.

        :param path:
            Path of video file
        :param label:
            Name of label that will house the player
        :param loop:
            If equal to 0, the video only plays once,
            if not it plays in an infinite loop (default 0)
        :param size:
            Changes the video's dimensions (2-tuple,
            default is 640x360)

    """

    def __init__(self, path, label, loop=0, size=(600, 350), controller=None, parent=None):
        self.imgFrames = []
        self.path = path
        self.label = label
        self.loop = loop
        self.size = size
        self.controller = controller
        self.parent = parent
        self.frame_data = imageio.get_reader(self.path)
        # resizes the video's frames and stores them in a list
        for image in self.frame_data.iter_data():
            self.imgFrames.append(ImageTk.PhotoImage(Image.fromarray(image).resize(self.size)))

    def load(self, label, loop):
        """
            Loads the video's frames recursively onto the selected label widget's image parameter.
            Loop parameter controls whether the function will run in an infinite loop
            or once.
        """
        if loop == 1:
            while True:
                for image in self.imgFrames:
                    label.configure(image=image)
                    label.image = image
                    sleep(0.05)
        else:
            for image in self.imgFrames:
                label.configure(image=image)
                label.image = image
                sleep(0.05)
            obj = SignupSqliteServices()
            if obj.checkLogin() == [(0,)]:
                self.parent.grid_configure(pady=(configure.screen_height - 600) / 2,
                                           padx=(configure.screen_width - 300) / 2)
                self.controller.showFrame("Login", self)
            else:
                self.parent.grid_configure(pady=0, padx=0)
                self.controller.showFrame("MainScreen", self)

    def play(self):
        """
            Creates and starts a thread as a daemon that plays the video by rapidly going through
            the video's frames.
        """
        thread = threading.Thread(target=self.load, args=(self.label, self.loop))
        thread.daemon = 1
        thread.start()
