import os
import pathlib


from .login_details import login
from .password_access import userpath, save_password, read_password

pathlib.Path.mkdir(pathlib.Path(f"{userpath}/data"), exist_ok=True)

if not os.path.isfile("pass.hash"):
    print("This first time will save your login details so remember them!!")