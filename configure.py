# Date    : 26/08/22 7:50 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import firebase_admin

dominant_color = '#1de9b6'
hyperlink_color = '#212121'
non_dominant_color = '#ffffff'
hover_color = '#1a1a1a'
screen_width = 0
screen_height = 0
font = 'Roboto-Regular'
config = {
            "apiKey": "AIzaSyDpP2ojp2bAUNVEpHXajw3m5jW7t6EJ8ME",
            "authDomain": "kongknitec.firebaseapp.com",
            "projectId": "kongknitec",
            "storageBucket": "kongknitec.appspot.com",
            "messagingSenderId": "440723985617",
            "appId": "1:440723985617:web:03c527e5fd79e6bf62a1f0",
            "measurementId": "G-Z89C7XHGZ3"
        }
app = firebase_admin.initialize_app(options=config)
