# 1. Name:
#    Hector Mendoza
# 2. Assignment Name:
#    Lab 02: Authentication
# 3. Assignment Description:
#    User authentication algorithm, controlling the login flow
#    and permission to access a "member only" program.
#    User is asked to enter a username and password in other
#    to get authenticated and gain access to the program.
# 4. What was the hardest part? Be as specific as possible.
#    Program structure in order to be organized.
#    I feel like I have implemented too many while loops
#    in order to continue the "input flow" if data is entered
#    incorrectly. Not sure if this is the standard in the industry?
# 5. How long did it take for you to complete the assignment?
#    2.5 hours

import json

# main() function controlling our login flow
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
                # We make sure to authenticate the user before we login
                valid_user = False
                while not valid_user:
                    username = input("Username: ")
                    password = input("Password: ")
                    valid_user = authenticate(data, username, password)
                
                login(username)

# We load our 'database' from our json file
def get_data():
    # File is closed when the block inside the with statement
    # is done executing
    try:
        with open('Lab02.json', 'r') as json_file:
            data = json.load(json_file)

        return data
    except:
        print("Unable to open file lab02.json.")
        return False

# We authenticate our user against our 'database'
def authenticate(data, username, password):
    usernames = data['username']
    passwords = data['password']

    # we make sure the username is in our database
    if username in usernames:
        # now we make sure the password matches with the username
        # (correct index)
        i = usernames.index(username)
        if password == passwords[i]:
            print("You are authenticated!\n")
            return True
    
    print("You are not authorized to use the system.\n"
        "Incorrect username and/or password. Please try again.\n")
    return False

# Login functions after we have authenticated the user
def login(username):
    option = 0

    # Once the user is logged in, we show some account options
    while option != 2:
        print(f"Wecome to the system {username}. Please select an option:\n"
            "1. Change password.\n"
            "2. Logout.\n")
        option = int(input('> '))

        if option == 1:
            change_password(username)

# Change current password function
def change_password(username):
    print("Implement change password function here...\n")

if __name__ == "__main__":
    main()