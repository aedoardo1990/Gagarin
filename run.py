import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Google sheets credentials and worksheet data - code from Code Institute Love Sandwiches Project
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('gagarin_quiz')

# retrieve columns of worksheet and its values - code from https://github.com/Boiann/space-quiz/tree/main
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

# Welcome message
print("Hello and welcome to Soviet Union!\n")
print("You are right, USSR is dead but it still lives in the memory of its today's nostalgic supporters\n")
print("Do you want to be our comrade? If yes, please enter a name to start the quiz and revive our glorious past.\n")

while True: 
    username = input("")
    if not username:
        print("Blank username is invalid. Please enter letters, numbers or combination of both as username.\n")
        continue 
    else:
        print("приве́т," + username + "!")
        break
