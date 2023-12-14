import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, Back, Style

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
data1 = questions.get_all_values()

answers = SHEET.worksheet('answers')
data2 = answers.get_all_values()

hints = SHEET.worksheet('hints')
data3 = hints.get_all_values()

soviet_story = SHEET.worksheet('soviet_story')
data4 = soviet_story.get_all_values()

player_scores = SHEET.worksheet('player_scores')
data5 = player_scores.get_all_values()

# map questions from Google Sheet - dictionary
questions = {
    question[0][0]: 'A',
    question[1][0]: 'B',
    question[2][0]: 'C'
}

# map answers from Google Sheet - list of lists
answers = [
    [answer[0][0], answer[0][1], answer[0][2]],
    [answer[1][0], answer[1][1], answer[1][2]],
    [answer[2][0], answer[2][1], answer[2][2]]
]

# map hints from Google Sheet - dictionary
hints = {
    hint[0][0],
    hint[1][0],
    hint[2][0]
}

# map soviet story from Google Sheet - dictionary
soviet_stories = hints = {
    story[0][0],
    story[1][0],
    story[2][0]
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
    if rules == "Y":
        print("\nHere are the instructions:\n")
        print("★ Choose the correct answer among the options A), B), C)")
        print("★ If the answer is correct you will receive 10 points")
        print("★ If the answer is incorrect you will receive 0 points")
        print("★ If you want a Hint before choosing the answer, pls enter H\n")
        break
    elif rules == "N":
        print("\nLet's play!")
        break
    else:
        print(f"\n{Fore.RED}Choice is invalid, please enter Y or N{Fore.WHITE}\n")
        continue

def start_quiz():
    """
    Function starts the quiz
    """
