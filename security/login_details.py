from fernet import Fernet
from getpass import getpass

from . import password_check

def login():
    username = input("Username: ")
    while " " in username:
        print("Username cannot contain spaces!")
        username = input("Username: ")
    password = getpass("Password: ")
    result = password_check.password_check(username, password)
    return result



