import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, Back, Style
from tabulate import tabulate
from simple_colors import *

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Google sheets credentials & worksheet data - code of Love Sandwiches Project
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('soviet_union_quiz')

# retrieve cols worksheet & vals-https://github.com/Boiann/space-quiz/tree/main
questions = SHEET.worksheet('questions')
question = questions.get_all_values()

answers = SHEET.worksheet('answers')
answer = answers.get_all_values()

hints = SHEET.worksheet('hints')
hints = hints.get_all_values()

soviet_story = SHEET.worksheet('soviet_story')
soviet_s = soviet_story.get_all_values()

comrade_scores = SHEET.worksheet('comrade_scores')
score = comrade_scores.get_all_values()

# map questions from Google Sheet - dictionary
questions = {
    question[0][0]: 'C',
    question[1][0]: 'B',
    question[2][0]: 'A'
}

# map answers from Google Sheet - list of lists
answers = [
    [answer[0][0], answer[0][1], answer[0][2]],
    [answer[1][0], answer[1][1], answer[1][2]],
    [answer[2][0], answer[2][1], answer[2][2]]
]

# map hints from Google Sheet - dictionary
hints_show = [
    hints[0][0],
    hints[1][0],
    hints[2][0]
]

# map soviet story from Google Sheet - dictionary
soviet_stories = {
    soviet_s[0][0],
    soviet_s[1][0],
    soviet_s[2][0]
}

# Welcome message
print("Hello and welcome to Soviet Union!\n")
print("You are right, USSR is dead but it still lives in the memory of its")
print("today's nostalgic supporters. Do you want to be our comrade? If yes,")
print("please enter a name to start the quiz and revive our glorious past.\n")

while True:
    username = input("")
    if not username:
        print(f"{Fore.RED}Blank username is invalid. Please enter letters, numbers")
        print(f"or combination of both as username.\n{Fore.WHITE}")
        continue
    else:
        print("\nпривет, товарищ " + username + "!")
        break

print("\nDo you want to read the game rules? Y/N \n")

while True:
    rules = input("")
    rules = rules.upper()
    if rules == "Y":
        print("\nHere are the instructions:\n")
        print("★ Choose the correct answer among the options A), B), C)")
        print("★ If the answer is correct you will receive 10 points")
        print("★ If the answer is incorrect you will receive 0 points")
        print("★ If you want a Hint before choosing the answer, pls enter H")
        print("★ You can get more information about each topic question")
        print("  by entering Y after the choice has been made\n")
        break
    elif rules == "N":
        print("\nLet's play!\n")
        break
    else:
        print(f"\n{Fore.RED}Choice is invalid, please enter Y or N{Fore.WHITE}\n")
        continue


def start_quiz():
    """
    Function starts and runs the quiz
    """
    questions_answered = []
    correct_answers = 0
    question_n = 0

    for key in questions:
        print(key)

        for i in answer[question_n]:
            print(i)

        while True:
            question_answered = input("\nEnter A, B, C or H:\n")
            question_answered = question_answered.upper()
            if question_answered not in ('A', 'B', 'C', 'H'):
                print(f"\n{Fore.RED}Invalid input, enter A, B, C, or H{Fore.WHITE}\n")
            elif question_answered == "H":
                for hint_choice in hints_show:
                    if hint_choice == hints[question_n][0]:
                        print(f"{Fore.BLUE}{hint_choice}{Fore.WHITE}")
                        break
            else:
                break

        questions_answered.append(question_answered)
        correct_answers += answer_check(questions.get(key), question_answered)
        while True:
            reply = input("Do you want to know more about this topic?\n")
            reply = reply.upper()
            if reply == "Y":
                for story in soviet_stories:
                    if story == soviet_s[question_n][0]:
                        print(f"\n{Fore.GREEN}{story}{Fore.WHITE}\n")
                break
            elif reply == "N":
                print("\nхорошо, пойдем!\n")
                break
            else:
                print(f"\n{Fore.RED}Invalid input, pls enter Y or N.{Fore.WHITE}\n")
                continue

        question_n += 1
    print(f"\nYou got {correct_answers} points out of 30.")
    return correct_answers


def answer_check(correct_reply, question_answered): # credits to https://github.com/mikyrenato/3rd_Project_Quiz_Game/blob/main/run.py
    """
    function to check if the answer is correct and to calculate points
    """
    if question_answered == correct_reply:
        print("Correct товарищ, bravo!\n")
        return 10
    else:
        print(f"That's incorrect...Correct answer was {correct_reply}.\n")
        return 0


def points_counter(enter_scores): # credits to LoveSandwiches - Code Institute
    """
    function to update worksheet with final scores
    """
    print("\nUpdating leaderboard...\n")
    scores_worksheet = SHEET.worksheet("comrade_scores")
    scores_worksheet.append_row(enter_scores)
    print("Leaderboard updated successfully.\n")


def leaderboard(): # credits to https://www.askpython.com/python-modules/tabulate-tables-in-python
    """
    function displayes final leaderboard with player and score
    """
    scores_worksheet = SHEET.worksheet("comrade_scores")
    score = comrade_scores.get_all_values()

    def size(dat):
        return str(dat[1])

    score.sort(key=size, reverse=True)

    table = tabulate(score[0:11],headers=['Comrade name', 'Comrade score'],tablefmt='fancy_grid', stralign='center')
    colored_table = green(table) # colored table - credits to https://stackoverflow.com/questions/76734963/colorama-not-working-with-tabulate-to-display-colored-output-in-python

    print(colored_table) 


def restart_game():
    """
    function to restart the game
    """
    while True:
        restart = input("\nDo you want to play again? Enter Y or N\n")
        restart = restart.upper()
        if restart == "Y":
            start_quiz()
            points_counter(correct_answers)
            leaderboard()
        elif restart == "N":
            print("\nIt was nice having you among our comrades! Have a good day and life.\n")
            break
        else:
            print(f"\n{Fore.RED}Input is invalid, pls enter Y or N.{Fore.WHITE}\n")
            continue


enter_scores = start_quiz()
correct_answers = [str(username),int(enter_scores)]
points_counter(correct_answers)
leaderboard()
restart_game()





    