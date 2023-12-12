import gspread 
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Google sheets credentials and worksheet data
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('gagarin_quiz')

# retrieve columns of worksheet and its values 
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

print(data1)
print(data2)
print(data3)
print(data4)
print(data5)