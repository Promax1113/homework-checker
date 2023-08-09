from getpass import getpass

from security import login

if __name__ == "__main__":
    
    status = None

    while not status == "Access granted!" or status is None:
        username = input("Username: ")
        while " " in username:
            print("Username cannot contain spaces!")
            username = input("Username: ")
        status = login(username, getpass("Password: "))
        print(f"\n{status}\n")
        