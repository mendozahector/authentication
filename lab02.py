# 1. Name:
#    Hector Mendoza
# 2. Assignment Name:
#    Lab 02: Authentication
# 3. Assignment Description:
#    
# 4. What was the hardest part? Be as specific as possible.
#    
# 5. How long did it take for you to complete the assignment?
#    

import json

def main():
    option = 0

    while option != 2:
        print("Welcome. Please select an option:\n"
        "1. Login.\n"
        "2. Exit.\n")
        option = int(input('> '))

        if option == 1:
            # We continue if database was loaded successfully
            data = get_data()
            if data:
                valid_user = False
                while not valid_user:
                    username = input("Username: ")
                    password = input("Password: ")
                    valid_user = authenticate(data, username, password)
                
                login(username)

def get_data():
    # File is closed when the block inside the with statement
    # is done executing
    try:
        with open('lab02.json', 'r') as json_file:
            data = json.load(json_file)

        return data
    except:
        print("Unable to open file lab02.json.")
        return False

def authenticate(data, username, password):
    usernames = data['username']
    passwords = data['password']

    if username in usernames and password in passwords:
        return True
    else:
        print("You are not authorized to use the system.\n"
            "Incorrect username and/or password. Please try again.\n")
        return False

def login(username):
    option = 0

    while option != 2:
        print(f"Wecome to the system {username}. Please select an option:\n"
            "1. Change password.\n"
            "2. Logout.\n")
        option = int(input('> '))

        if option == 1:
            change_password(username)

def change_password(username):
    print("You will change your password:\n")

if __name__ == "__main__":
    main()