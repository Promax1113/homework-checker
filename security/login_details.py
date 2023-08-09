from fernet import Fernet
import hashlib

import os
import base64

from . import password_check

def login(username, password):
    result = password_check.password_check(username, password)
    if result == 403:
        return "Acess Denied!"
    elif result == 200:
        return "Access Granted!"
    elif result == "Saved login!":
        return result
    else:
        raise Exception(f"Password check returned {result} and did not match any option.") 


