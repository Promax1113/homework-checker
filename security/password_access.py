import base64
import hashlib
import pathlib
import os
from . import password_check
from fernet import Fernet

userpath = pathlib.Path(__name__).parent.resolve()


def gen_fernet_key(passcode: bytes) -> bytes:
    assert isinstance(passcode, bytes)
    hlib = hashlib.md5()
    hlib.update(passcode)
    return base64.urlsafe_b64encode(hlib.hexdigest().encode('latin-1'))


def save_password(_username, _password):
    
    f = Fernet(gen_fernet_key(password_check.user_details.encode("utf-8")))
    with open(f"{userpath}/data/passfile.passfile", "wb") as file:
        file.write(f.encrypt(bytes(_username, 'utf-8')))
        file.write(b"\n")
        file.write(f.encrypt(bytes(_password, 'utf-8')))
        file.close()
    return 200


def read_password():

    fernet_k = Fernet(gen_fernet_key(password_check.user_details.encode("utf-8")))

    with open(f"{userpath}/data/passfile.passfile", "r") as file:
        data = file.readlines()
        file.close()

    username = (fernet_k.decrypt(data[0].strip("\n").encode())).decode()
    password = (fernet_k.decrypt(data[1].encode())).decode()


    return {
        "username": username,
        "password": password
    }
