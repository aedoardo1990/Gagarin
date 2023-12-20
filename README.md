# Soviet Union Quiz

Welcome to Soviet Union Quiz! This quiz game was created for all the people enthusiastic and nostalgic about Soviet Union, for those who are interested to know some of its great achievements, culture and controversies. Churchill defined Russia as "a riddle, wrapped in a mystery, inside an enigma". Perhaps no better quote could define as well the history of USSR - of which Russia is its direct inheriter.
The project is dedicated to Yuri Gagarin, whose travel in space represents the peak of USSR glory. 

The game is a Python command-line terminal quiz, which runs in the Code Institute mock terminal on Heroku.

The link to our Live Website can be found here - [Soviet Union Quiz](https://soviet-union-8544d8a31c4f.herokuapp.com/).

![Responsive Mockup](assets/images/readme/mockup_1.png)


## Index - Table of Contents

- [Planning](#planning)
- [Design](#design)
- [UX](#ux)
    - [Programm Goals](#programm-goals)
    - [User Stories](#user-stories)
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#possible-future-features)
- [Data Model](#data-model)
- [Testing](#testing)
    - [Validator Testing](#validator-testing)
    - [Browser Testing](#browser-testing)
    - [Testing User Stories](#testing-user-stories-functionality)
- [Debugging](#debugging)
    - [Fixed bugs](#fixed-bugs)
    - [Unfixed bugs](#unfixed-bugs)
- [Deployment](#deployment)
- [Credits](#credits)
    - [Data](#data)
    - [Code](#code)
    - [Styling](#styling)


## Planning

The project was firstly conceived through the creation of the following diagram. It was created with [lucidchart.com](https://www.lucidchart.com/). 

![Diagram](TO CORRECT AND UPLOAD PHOTO)


## Design

### Color scheme

Since this is a simple terminal based application, the design process for the user interface was limited.

Different colors are used to categorize different types of messages displayed to the user:
- Red -> error due to invalid input given by the user to the programm 
- Blue -> hints to help the user to answer each question
- Green -> correct answer given by the user to a quiz question
- Red -> incorrect answer given by the user to a quiz question
- Cyan -> after choosing an answer to a question, the user has the option to get a few more information about the topic, which is highlighted in cyan color

Red color is used as well for the 2 ASCII art images at the start of the quiz, for the leaderboard at the end and for the red star (present in the header of the quiz, in the first text based screen of the programm and in the instructions). The choice of red as the predominant color aims at recalling the color of the flag of Soviet Union. 

### Imagery

- The red star is one of the most famous symbols of USSR - its meaning is explained in one of the questions of the quiz, therefore no spoilers will be done here. Still today in Moscow, there are some state buildings with the red star on top.
FOTO TO UPLOAD
- In the second ASCII ART image there is Yuri Gagarin. By achieving the major milestone to be the first cosmonaut in space for Soviet Union amidst the Space Race, he became an international celebrity and was awarded many medals and titles, including the nation's highest distinction: Hero of the Soviet Union.
FOTO TO UPLOAD
- The favicon is another well known symbol of Soviet Union, which is the hammer and the sieckle. It represents the proletarian solidarity between agricultural and industrial workers. It was first adopted during the Russian Revolution at the end of World War I, the hammer representing workers and the sickle representing the peasants.

<img src="assets/images/favicon.jpeg" height="140" width="150">

### Typography 

- The font chosen for the title "Soviet Union Quiz" is "Russo One". Russo One was chosen because it is a Unicode typeface family that supports languages that use the Cyrillic, Baltic, Turkish, Central Europe, Latin script and its variants. 
FOTO TO UPLOAD
- The font chosen for the first ASCII image is Buran. The font is dedicated to the memory of the Soviet Space Shuttle named Buran - for more information click <a href="https://en.wikipedia.org/wiki/Buran_%28spacecraft%29" target="_blank" rel="noopener" aria-label="Check the Buran page of Wikipedia">here</a>. 
Source of the font is https://www.dafont.com/buran-ussr.font


## UX

### Programm Goals

The programm aims at providing the user with a simple and intuive multiple choice quiz game, which can be repeated as many times as the user wants. 

### User Stories

**As a user I want to:**

- have an intro image to get into the atmosphere of Soviet Union 
- be able to read a short introduction about the quiz when it first loads 
- be able to enter a username 
- be alerted by the programm if no username was entered from my side
- be able to have the choice to read or not the instructions before playing the game 
- have the choice to get hints before answering questions of which I don't know the answer
- have the option to choose straight away the answer among A) B) or C) option, if I don't want to get any hint
- be alerted by the programm if I have not entered any of the valid option after a question, which should be A), B), C) or H)
- be alerted by the programm if I have answered correctly
- be alerted by the programm if I have NOT answered correctly and to know which answer was the correct one
- have the option to get further information about the question topic after replying to it or to skip that
- have time to read the additional information and choose when to proceed with the next question
- get an error message if the input to the just mentioned option was incorrect
- get a total score of my points at the end of the game
- get displayed a leaderboard at the end of the game to see hpw my score ranks compared to other players
- get the option at end of the game to play again
- play again without the need to read again the instructions
- repeat the game as many times as I wish
- have the choice to quit the game after finishing it
- get a good-bye message when quitting the game


** As a site administrator I want to **
- be able to make modifications to the game (see [future features](#future-features))
- offer the user with a short, entertaining and informative game


## Testing

### Testing User Stories (Functionality)

| Expectation (As a user, I want to...)  | Result (As a user, I...)    |
| :---------------------------------: | :------------------------------:|
| have an intro image to get into the atmosphere of Soviet Union | have a beautiful intro image with Yuri Gagarin in space suit |
| be able to read a short introduction about the quiz when it first loads | have a short coincise introduction at the start of the game |
| be able to enter a username | can enter a username |
| be alerted by the programm if no username was entered from my side | get an error message if I didn't enter a username |
| be able to have the choice to read or not the instructions before playing the game | can choose to read or to skip the instructions | 
| have the choice to get hints before answering questions of which I don't know the answer | have the option to get hints for each question |
| have the option to choose straight away the answer among A) B) or C) option, if I don't want to get any hint | can reply to each question without the need to get a hint |
| be alerted by the programm if I have not entered any of the valid option after a question, which should be A), B), C) or H) | get an error message when my input is invalid |
| be alerted by the programm if I have answered correctly | get a congratulation message when I answer correctly |
| be alerted by the programm if I have NOT answered correctly and to know which answer was the correct one | get informed if my answer was incorrect and which option was the correct one  |
| have the option to get further information about the question topic after replying to it or to skip that | have the opportunity to get more information about each topic question and to deepen my Soviet knowledge |
| have time to read the additional information and choose when to proceed with the next question | have all the time I need to read the additional facts about Soviet Union and can choose when to go to the next question |
| get a total score of my points at the end of the game | get a score of my points at the end of the quiz |
| get a leaderboard at the end of the game to see how my score ranks compared to other players | get a leaderboard at the end of the quiz where I can see how my performance ranks among all previous players |
| get the option at end of the game to play again | have the option to play again at the end of the quiz |
| play again without the need to read again the instructions | don't get the option to read again the instructions when I decide to play again |
| repeat the game as many times as I wish | can repeat the game endlessly |
| have the choice to quit the game after finishing it | can quit the game after replying to all the questions |
| get a good-bye message when quitting the game | get a good-bye message when I choose to quit the game |












