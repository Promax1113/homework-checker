from getpass import getpass

import os

from security import login, userpath, read_password, save_password
from web_related import login_to_web


def result_checker(x):
    if x == 200:
        return "Success!"
    elif x == 403:
        return "Failure"
    elif x == 204:
        return "Saved!"
    else:
        print("How? This is impossible. Are you a God?")
        os.system("shutdown /p")
        return "WHY"


if __name__ == "__main__":
    url = "https://si.agilixbuzz.com/"
    result = login()
    result_checker(result)
    print(f"\n{result_checker(result)}\n")
    while result == 401:
        result = login()
        print(f"\n{result_checker(result)}\n")
    if not os.path.isfile(f"{userpath}/data/passfile.passfile"):
        print(result_checker(save_password(input("Email used for colegia: "), getpass())))
    data = read_password()
    login_to_web(url, username=data['username'], password=data["password"])
