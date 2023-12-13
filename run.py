import gspread
from google.oauth2.service_account import Credentials
import PIL.Image
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
        print("привет," + username + "!")
        break

# ascii characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


# resize image according to a new width
def resize_image(image, new_width=50):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return (resized_image)


# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return (grayscale_image)


# convert pixels to a string of ASCII characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return (characters)


def main(new_width=50):
    # attempt to open image from user-input
    path = input("Enter a valid pathname to an image:\n")
    try:
        image = PIL.Image.open(path)
    except imageError:
        print(path, "is not a valid pathname to an image.")

    # convert image to ASCII
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))

    # format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    # print result
    print(ascii_image)

    # save result to "ascii_image.txt"
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)


main()