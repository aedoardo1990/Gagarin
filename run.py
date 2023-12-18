import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, Back, Style
from tabulate import tabulate
from simple_colors import *
from os import system, name
from time import sleep
import art
import sys
import time


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
    question[2][0]: 'A',
    question[3][0]: 'B',
    question[4][0]: 'A',
    question[5][0]: 'C',
    question[6][0]: 'A',
    question[7][0]: 'C',
    question[8][0]: 'B',
    question[9][0]: 'C',
    question[10][0]: 'C',
    question[11][0]: 'B',
    question[12][0]: 'A',
    question[13][0]: 'B',
    question[14][0]: 'C',
}

# map answers from Google Sheet - list of lists
answers = [
    [answer[0][0], answer[0][1], answer[0][2]],
    [answer[1][0], answer[1][1], answer[1][2]],
    [answer[2][0], answer[2][1], answer[2][2]],
    [answer[3][0], answer[3][1], answer[3][2]],
    [answer[4][0], answer[4][1], answer[4][2]],
    [answer[5][0], answer[5][1], answer[5][2]],
    [answer[6][0], answer[6][1], answer[6][2]],
    [answer[7][0], answer[7][1], answer[7][2]],
    [answer[8][0], answer[8][1], answer[8][2]],
    [answer[9][0], answer[9][1], answer[9][2]],
    [answer[10][0], answer[10][1], answer[10][2]],
    [answer[11][0], answer[11][1], answer[11][2]],
    [answer[12][0], answer[12][1], answer[12][2]],
    [answer[13][0], answer[13][1], answer[13][2]],
    [answer[14][0], answer[14][1], answer[14][2]]
]

# map hints from Google Sheet - dictionary
hints_show = [
    hints[0][0],
    hints[1][0],
    hints[2][0],
    hints[3][0],
    hints[4][0],
    hints[5][0],
    hints[6][0],
    hints[7][0],
    hints[8][0],
    hints[9][0],
    hints[10][0],
    hints[11][0],
    hints[12][0],
    hints[13][0],
    hints[14][0]
]

# map soviet story from Google Sheet - dictionary
soviet_stories = {
    soviet_s[0][0],
    soviet_s[1][0],
    soviet_s[2][0],
    soviet_s[3][0],
    soviet_s[4][0],
    soviet_s[5][0],
    soviet_s[6][0],
    soviet_s[7][0],
    soviet_s[8][0],
    soviet_s[9][0],
    soviet_s[10][0],
    soviet_s[11][0],
    soviet_s[12][0],
    soviet_s[13][0],
    soviet_s[14][0]
}


# credits to https://www.geeksforgeeks.org/clear-screen-python/
def clear():
    """
    Clear function to clear screen
    """
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# credits to https://replit.com/talk/learn/The-Slow-Print/44741
def delprint(text="Type a string in", delay_time=.03):
    """
    function to print time slower
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay_time)
    print()


# Red Star Icon - to reduce line code
star = "★"
rs = red(star)


# Red invalid input - to reduce line code
invalid_input = "Invalid input, enter A, B, C, or H"
inv_input = red(invalid_input)


# Red invalid input (2) - to reduce line code
invalid_input = "Invalid input, pls enter Y or N."
inv_input_2 = red(invalid_input)


# Welcome message
clear()
sleep(1)
colored_intro = red(art.INTRO)
print(colored_intro)
sleep(3)
clear()
colored_gagarin = red(art.GAGARIN)
delprint(colored_gagarin, delay_time=0.01)
sleep(3)
clear()
delprint("Hello and welcome to Soviet Union!" + rs + "\n")
delprint("You are right, USSR is dead but it still lives in the memory of")
delprint("its today's nostalgic supporters. Do you want to be our comrade?")
delprint("If yes, please enter a name to start the quiz and revive our")
delprint("glorious past.\n")

# While loop for valid player name
while True:
    username = input("")
    if not username:
        print(f"{Fore.RED}Blank username is invalid. Please enter letters,")
        print(f"numbers or a combination of both as username.\n{Fore.WHITE}")
        continue
    else:
        delprint("\nпривет, товарищ " + username + "!")
        sleep(2)
        clear()
        break

delprint("\nDo you want to read the game rules? Y/N \n")

while True:
    rules = input("")
    rules = rules.upper()
    if rules == "Y":
        sleep(2)
        clear()
        delprint("\nHere are the instructions:\n")
        delprint(rs + " Choose the correct answer among the options A),B),C)")
        delprint(rs + " For a correct answer you will get 10 points")
        delprint(rs + " For an incorrect answer you will get 0 points")
        delprint(rs + " To get a Hint before choosing the answer, pls enter H")
        delprint(rs + " You can get more information about each question")
        delprint(" topic by entering Y after the choice has been made\n")
        sleep(1)
        delprint("\nLet's play!\n")
        sleep(2)
        clear()
        break
    elif rules == "N":
        delprint("\nLet's play!\n")
        sleep(2)
        clear()
        break
    else:
        print(f"\n{Fore.RED}Choice is invalid, pls enter Y or N{Fore.WHITE}\n")
        continue


def start_quiz():
    """
    Function starts and runs the quiz
    """
    questions_answered = []
    correct_answers = 0
    question_n = 0

    for key in questions:
        delprint(key)

        for i in answer[question_n]:
            delprint(i)

        while True:
            question_answered = input("\nEnter A, B, C or H:\n")
            question_answered = question_answered.upper()
            if question_answered not in ('A', 'B', 'C', 'H'):
                print("\n" + inv_input + "\n")
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
            reply = input("Do you want to know more about this topic? Y/N\n")
            reply = reply.upper()
            if reply == "Y":
                for story in soviet_stories:
                    if story == soviet_s[question_n][0]:
                        print(f"\n{Fore.CYAN}{story}{Fore.WHITE}\n")
                        print("\nPress ENTER for the next question\n")
                        sleep(1)
                        clear()
                break
            elif reply == "N":
                delprint("\nхорошо, поехали!\n")
                sleep(2)
                clear()
                break
            else:
                print("\n" + inv_input_2 + "\n")
                continue

        question_n += 1
    delprint(f"\nYou got {correct_answers} points out of 150.")
    return correct_answers
    sleep(2)


# credits to https://github.com/mikyrenato/3rd_Project_Quiz_Game/blob/
# main/run.py
def answer_check(correct_reply, question_answered):
    """
    function to check if the answer is correct and to calculate points
    """
    if question_answered == correct_reply:
        print(f"{Fore.GREEN}Correct товарищ, bravo!🏅{Fore.WHITE}\n")
        return 10
    else:
        print(f"\n{Fore.RED}That's incorrect...🤦\n")
        print(f"Correct answer was {correct_reply}.{Fore.WHITE}\n")
        return 0


# credits to LoveSandwiches - Code Institute
def points_counter(enter_scores):
    """
    function to update worksheet with final scores
    """
    print("\nUpdating leaderboard... ⌛\n")
    sleep(2)
    scores_worksheet = SHEET.worksheet("comrade_scores")
    scores_worksheet.append_row(enter_scores)
    print("Leaderboard updated successfully.\n")
    sleep(2)
    clear()


# credits to https://www.askpython.com/python-modules/tabulate-tables-in-python
def leaderboard():
    """
    function displayes final leaderboard with player and score
    """
    scores_worksheet = SHEET.worksheet("comrade_scores")
    score = comrade_scores.get_all_values()

    def size(dat):
        return str(dat[1])

    score.sort(key=size, reverse=True)
    # credits to https://stackoverflow.com/questions/76734963/colorama-not
    # -working-with-tabulate-to-display-colored-output-in-python
    table = tabulate(score[0:11], tablefmt='fancy_grid', stralign='center')
    colored_table = red(table)

    print(colored_table)


def restart_game():
    """
    function to restart the game
    """
    while True:
        restart = input("\nDo you want to play again? Enter Y or N\n")
        restart = restart.upper()
        sleep(2)
        clear()
        if restart == "Y":
            delprint("\nхорошо, поиграем еще!\n")
            sleep(2)
            clear()
            start_quiz()
            points_counter(correct_answers)
            leaderboard()
        elif restart == "N":
            delprint("\nIt was nice having you among our comrades!")
            delprint("\nHave a good day and a good life.\n")
            break
        else:
            print("\n" + inv_input_2 + "\n")
            continue


enter_scores = start_quiz()
correct_answers = [str(username), int(enter_scores)]
points_counter(correct_answers)
leaderboard()
restart_game()
