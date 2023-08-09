

from security import login

if __name__ == "__main__":
    
    print(lambda x: "Access granted!" if login() == 200 else)