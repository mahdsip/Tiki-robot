# -*- coding: utf-8-*-
import random
import re
from subprocess import call

WORDS = ["TURN", "LEFT"]


def handle(text, mic, profile):
    """
        send I2C signal to arduino to turn left
    """

    messages = ["going left",
                "left left",
		"turning left"]

    message = random.choice(messages)


    mic.say(message)

    call(["/home/pi/main", "5"])

def isValid(text):
    """
        Returns True if the input is related to turn left.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bturn left\b', text, re.IGNORECASE))

