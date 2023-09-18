import hashlib

import os

from . import save_login

user_details = None

def password_check(username, password):
    if os.path.isfile("pass.hash"):
        global user_details
        pass_user = username + password
        pass_user_hash = hashlib.sha256(bytes(pass_user, "utf-8"))
        user_details = pass_user

        with open("pass.hash", "r") as f:
            file_pass = f.readline()
            f.close()

        if pass_user_hash.hexdigest() == file_pass:
            return 200
        else:
            return 401
    else:
        return save_login.save_login_details(password=password, username=username)