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
    data = get_data()

    # We continue if database was loaded successfully
    if data:
        username = input("Username: ")
        password = input("Password: ")

        authenticate(data, username, password)

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
        print("we have a match!")
    else:
        print("error login in.")

if __name__ == "__main__":
    main()