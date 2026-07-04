"""
utils.py

Utility helper functions.
"""

import datetime

def get_timestamp():

    return datetime.datetime.now()

def log(message):

    print(f"[INFO] {get_timestamp()} : {message}")
