from user_functions import *
from quiz_functions import *


if __name__ == '__main__':
    
    Run = True
    while Run:
        
        user = startLoginSection()
        print(f"\nLogged in as \"{user.username}\", last time played -> {user.date}, latest result -> {user.latest_result}\n")
        startQuizSection(user)
        
