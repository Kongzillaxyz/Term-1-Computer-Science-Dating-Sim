import shutil
import textwrap
import time

#Up the questionAsking by 1 for each question, and set it to 0 when no longer using.
questionAsking = 1

#Use the message variable and the printMessage function when you want to print something
#to console, instead of using the print command.
#this function gets the console size and makes a new line when a word would cut off.
def printMessage():
  global message
  print(textwrap.fill(message, width=shutil.get_terminal_size().columns))


message = ("Welcome to I Havent Thought of a Name! This is an extravagant Dating Sim where you will date many questionable people! If you're ready to begin, we can go onto the questionnaire!")
printMessage()

while questionAsking == 1:
  playerName = input("\nMy name is... ")
  if playerName == "":
    print("Please enter a name.")
  elif len(playerName) < 3:
    print("Name must be at least 3 letters long.")
  elif len(playerName) > 16:
    print("Name is to long; please try again.")
  else:
    stringHasNumber = False
    stringHasSpecialCharacter = False

    for i in playerName:

      #If inputted string has any of these characters, set flag to true
      if i in "!@#$%^&*()+_-=\|]}[{:;/><~":
        stringHasSpecialCharacter = True

      if i in "0123456789":
        stringHasNumber = True

    if stringHasSpecialCharacter is True or stringHasNumber is True:
      message = ("Name must not contain numbers or special characters")
      printMessage()
    else:
      print("Welcome, " + playerName + "! Let's continue.")
      questionAsking = questionAsking + 1


while questionAsking == 2:
  try:
    Age = int(input("How old are you? "))
    if Age < 13:
      message = ("You are not old enough to date! Also you should not be playing this game. Please lie next time!")
      printMessage()
      exit()

    elif Age < 16:
      message = ("Happy Birthday because you're 16 now! Enjoy your new found age!")
      printMessage()
      questionAsking = questionAsking + 1

    elif Age == 17 or Age == 18:
      message = ("You're 16 again! Amazing! The other years must have been a dream!")
      printMessage()
      questionAsking = questionAsking + 1

    elif Age > 18:
      message = ("Too bad! You're in High School again! Welcome back to 16 years old!")
      printMessage()
      questionAsking = questionAsking + 1
    
  except ValueError:
    print("That is not a valid age! Please try again!")


while questionAsking == 3:
  print("placeholderText")
