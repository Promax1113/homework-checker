from getpass import getpass

import os

from security import login, userpath, read_password, save_password

if __name__ == "__main__":
    result = login()
    f = lambda x: "Success!" if x == 200 else ("Failure!" if x == 403 else ("Saved your password!" if x == 204 else print("Invalid!")))
    print(f"\n{f(result)}\n")
    while f(result) == "Failure!":
        result = login()
        print(f"\n{f(result)}\n")
    if not os.path.isfile(f"{userpath}/data/passfile.passfile"):
        print(f(save_password(input("Email used for colegia:"), getpass())))
