# -*- coding: utf-8-*-
import random
import re
from subprocess import call

WORDS = ["TURN", "RIGHT"]


def handle(text, mic, profile):
    """
        send I2C signal to arduino to turn left
    """

    messages = ["going right",
                "left right",
		"turning right"]

    message = random.choice(messages)


    mic.say(message)

    call(["/home/pi/main", "6"])

def isValid(text):
    """
        Returns True if the input is related to turn left.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bturn right\b', text, re.IGNORECASE))

