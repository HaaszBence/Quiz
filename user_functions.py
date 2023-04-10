import global_functions
from random import randint

class User:
    
    def __init__(self, username, password, date, latest_result=0, best_result=0):
        self.username = username
        self.password = password
        self.date = date
        self.latest_result = int(latest_result)
        self. best_result = int(best_result)



def getAlternativeUsernames(username, usernames_in_use):
    alt_usernames = []
    max_number = 0

    while len(alt_usernames) < 3:
        max_number += 1
        alt_username = username + str(randint(1,max_number))
        if alt_username not in alt_usernames and alt_username not in usernames_in_use:
            alt_usernames.append(alt_username)
    
    return alt_usernames


def createUsername():
    file = global_functions.breakToLines('Data/Users.txt')
    usernames_in_use = [line.split('; ')[0] for line in file]
    
    username = input("Username: ")
    alternative_usernames = getAlternativeUsernames(username, usernames_in_use)

    while username in usernames_in_use:
        print("\nThis username is already taken. Here are some alternatives: ")
        print(*alternative_usernames, sep='; ')
        print("")
        username = input("Username: ")
        alternative_usernames = getAlternativeUsernames(username, usernames_in_use)
    
    return username


def createUserpassword():
    done = False
    
    while not done:
        print("\nPassword length must be between 5-10 characters\n")
        password = input("Password: ")
        password_conf = input("Confirm password: ")

        if password == password_conf and len(password) <= 10 and len(password) >= 5:
            done = True
        elif password != password_conf:
            print("\nNot matching password")
        elif len(password) <= 10 and len(password) >= 5:
            print("\nCharecter length does not match the criteria")

    return password


def createUser():
    username = createUsername()
    password = createUserpassword()
    date = global_functions.currentTime()
    user = User(username, password, date)

    with open('Data/Users.txt', 'at', encoding='utf-8') as file:
        file.write(f'{user.username}; {user.password}; {user.date}; {user.latest_result}; {user.best_result}\n')
    
    return loginUser(username, password)


def loginUser(inp_username, inp_password):
    
    found_user = False

    for line in global_functions.breakToLines('Data/Users.txt'):
        user_data = line.split('; ')
        line_username = user_data[0]
    
        if line_username == inp_username:
            line_password = user_data[1]
    
            if line_password == inp_password:
                user = User(user_data[0], user_data[1], user_data[2], user_data[3], user_data[4])
                found_user = True
                break

    if found_user:
        return user
    else:
        print(f"\nNo user found named \"{inp_username}\" with matching password!\n")


def getLoginData():
    username = input("Username: ")
    password = input("Password: ")
    login_data = [username, password]

    return login_data


def refreshUserData(user):
    users_file = global_functions.breakToLines('Data/Users.txt')
    
    for line in users_file:
        if line.split('; ')[0] == user.username:
            users_file.remove(line)
            break
    
    with open('Data/Users.txt', 'wt', encoding='utf-8') as file:
    
        for line in users_file:
            user_data = line.split('; ')
            file.write(f'{user_data[0]}; {user_data[1]}; {user_data[2]}; {user_data[3]}; {user_data[4]}\n')
        file.write(f'{user.username}; {user.password}; {user.date}; {user.latest_result}; {user.best_result}\n')


def startLoginSection():
    print('\n------------------------WELCOME TO THE QUIZ GAME------------------------\n')
    log_reg = input("Would you like to login(LOG) or register(REG) as a new user? ").upper()

    while log_reg != 'REG' and log_reg != 'LOG':
        log_reg = input("\nPlease choose from the following options: 'LOG' for login or 'REG' for registration: \n").upper()
    
    if log_reg == 'REG':
        print('\n-----------------------------REGISTRATION-----------------------------\n')
        user = createUser()
    else:
        print('\n----------------------------------LOGIN----------------------------------\n')
        tries = 3
        user = None
        
        while tries > 0 and user == None:
            login_data = getLoginData()
            user = loginUser(login_data[0], login_data[1])
            tries -= 1
        
        if tries == 0:
            print("\nCouldn't find user 3 time, now directing to registration.\n")
            createUser()
    
    return user