# Date    : 02/09/22 10:30 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import os
import uuid
from dotenv import load_dotenv
from firebase_admin import auth

from configure import app


class FirebaseFunc:
    @staticmethod
    def fireAuth():
        # load_dotenv()
        # APIKEY = os.getenv('apikey')
        # AUTHDOMAIN = os.getenv('authdomain')
        # PROJECTID = os.getenv('projectid')
        # STORAGEBUCKET = os.getenv('storagebucket')
        # MESSAGINGSENDERID = os.getenv('messagingsenderid')
        # APPID = os.getenv('appid')
        # MEASUREMENTID = os.getenv('measurementid')
        token = auth.create_custom_token(uuid.uuid1(), app=app)
        user = auth.verify_id_token(token, app=app)
        print(user)
        # firebase = Firebase(config)
        # auth = firebase.auth()
        # token = auth.create_custom_token(uuid.uuid1())
        # user = auth.sign_in_with_custom_token(token)
        # print(user)
