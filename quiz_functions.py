import global_functions
from user_functions import refreshUserData
from random import randrange

def getQuestions():
    selected_questions = []
    file = global_functions.breakToLines('Data/Questions.txt')
    questions = [line.split('; ')[0] for line in file]

    while len(selected_questions) < len(questions):
        selected_questions.append(questions[randrange(0, len(questions))])

    return selected_questions


def changeUserValue(user_answer):
    if user_answer == 'A':
            user_answer = 1
    elif user_answer == 'B':
        user_answer = 2
    elif user_answer == 'C':
        user_answer = 3
    elif user_answer == 'D':
        user_answer = 4
    return user_answer


def getQuestionChoicesAndAnswer(question):
    file = global_functions.breakToLines('Data/Questions.txt')
    for line in file:
        if line.split('; ')[0] == question:
            choices = line.split('; ')[1:5]
            answer = line.split('; ')[5]
    return choices, answer


def startQuizSection(user):

    result = 0
    print('\n----------------------------------QUIZ----------------------------------\n')
    questions = getQuestions()

    for question in questions:
        print(f"\n{question}\n")
        choices, correct_answer = getQuestionChoicesAndAnswer(question)
        print(f"A, {choices[0]};   B, {choices[1]}\nC, {choices[2]};   D, {choices[3]}\n")
        user_answer = changeUserValue(input("Your answer(A, B, C, D): ").upper())

        if user_answer == int(correct_answer):
            result += 1
            print("\nCorrect answer!\n")
        else:
            print("\nIncorrect answer!\n")
            break

    if result > user.best_result:
        user.best_result = result
        print("New record set!")
        print(f"Your points -> {result}")
    else:
        print(f"Your best result -> {user.best_result}")
        print(f"Your points -> {result}")
    user.latest_result = result
    user.date = global_functions.currentTime()
    refreshUserData(user)