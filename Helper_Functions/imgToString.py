# Date    : 22-03-2023 12:30
# Author  : DENCODER (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0

import base64


def imgToStringConverter(path):
    with open(path, "rb") as img_file:
        strImg = base64.b64encode(img_file.read())
    return strImg


def stringToImgConverter(strImg, path):
    image = open(path, "wb")
    image.write(base64.b64decode(strImg))
    image.close()
