from getpass import getpass
import schedule

import os

from security import login, userpath, read_password, save_password
from web_related import login_to_web

if __name__ == "__main__":
    url = "https://si.agilixbuzz.com/"
    result = login()
    f = lambda x: "Success!" if x == 200 else ("Failure!" if x == 403 else ("Saved your password!" if x == 204 else print("Invalid!")))
    print(f"\n{f(result)}\n")
    while f(result) == "Failure!":
        result = login()
        print(f"\n{f(result)}\n")
    if not os.path.isfile(f"{userpath}/data/passfile.passfile"):
        print(f(save_password(input("Email used for colegia: "), getpass())))
    data = read_password()
    login_to_web(url, username=data['username'], password=data["password"])