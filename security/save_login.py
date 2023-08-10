import hashlib

import base64

def save_login_details(username, password):
    with open('pass.hash', "w+") as f:
        pass_text = username + password
        pass_hash = hashlib.sha256(bytes(pass_text, "utf-8"))
        f.write(pass_hash.hexdigest())
        f.close()
    return 204


