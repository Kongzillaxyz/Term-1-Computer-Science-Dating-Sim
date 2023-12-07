import shutil
import textwrap

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
      if i in "!@#$%^&*()+_-=\\|]}[{:;/><~.,/~`*":
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
    message = ("How old are you? ")
    printMessage()
    Age = int(input(""))
    if Age < 13:
      message = ("You are not old enough to date! Also you should not be playing this game. Please lie next time!")
      printMessage()
      exit()

    elif Age < 16:
      message = ("Happy Birthday because you're 16 now! Enjoy your new found age!")
      printMessage()
      questionAsking = questionAsking + 1

    elif Age == 16:
      message = ("Perfect!")
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
    message = ("That is not a valid age! Please try again!")
    printMessage()

noLoopFlag = False
#Coding Judged
while questionAsking == 3:
  try:
    while noLoopFlag is False:
      message = ("1: She/Her 2: He/Him 3: They/Them 4: She/They 5: He/They 6: She/Him 7: She/They/Him")
      printMessage()
      message = ("\nWhat are your preferred pronouns from these options?")
      printMessage()
      noLoopFlag = True
    Pronouns = int(input(""))
    if Pronouns == 1:
      #Pronouns changed to match option for simplicity
      Pronouns = "She/Her"
      #choosen Pronouns should not be capitilized
      choosenPronounOne = "she"
      choosenPronounTwo = "her"
      questionAsking = questionAsking + 1

    elif Pronouns == 2:
      Pronouns = "He/Him"
      choosenPronounOne = "he"
      choosenPronounTwo = "him"
      questionAsking = questionAsking + 1

    elif Pronouns == 3:
      Pronouns = "They/Them"
      choosenPronounOne = "they"
      choosenPronounTwo = "them"
      questionAsking = questionAsking + 1

    elif Pronouns == 4:
      Pronouns = "She/They"
      choosenPronounOne = "she"
      choosenPronounTwo = "they"
      questionAsking = questionAsking + 1

    elif Pronouns == 5:
      Pronouns = "He/They"
      choosenPronounOne = "he"
      choosenPronounTwo = "they"
      questionAsking = questionAsking + 1

    elif Pronouns == 6:
      Pronouns = "She/Him"
      choosenPronounOne = "she"
      choosenPronounTwo = "him"
      questionAsking = questionAsking + 1

    elif Pronouns == 7:
      Pronouns = "She/They/Him"
      choosenPronounOne = "she"
      choosenPronounTwo = "they"
      choosenPronounThree = "him"
      questionAsking = questionAsking + 1

    else:
      message = ("Thats not a valid answer. Please choose a number from 1 to 7.")
      printMessage()
  except ValueError:
    message = ("That is not a valid answer! Please choose a number from 1 to 7.")
    printMessage()
    #while writing, use choosenPronounOne when you would say "She", "He", or "They"
    #Then use choosenPronounTwo when you would say "Her", "Him", or "Them"
noLoopFlag = False
while questionAsking == 4:
  try:
    while noLoopFlag is False:
      message = ("Great! Now, please choose your gender preference from the following options\n")
      printMessage()
      message = ("1. Male  2. Female  3. Nonbinary  4. No Preference")
      printMessage()
      noLoopFlag = True
    genderPreference = int(input(""))
    if genderPreference == 1:
      genderPreference = "male"
      questionAsking = questionAsking + 1
    elif genderPreference == 2:
      genderPreference = "female"
      questionAsking = questionAsking + 1
    elif genderPreference == 3:
      genderPreference = "nonbinary"
      questionAsking = questionAsking + 1
    elif genderPreference == 4:
      genderPreference = "no preference"
      questionAsking = questionAsking + 1
    else:
      message = ("Thats not a valid answer. Please choose a number from 1 to 4.")
      printMessage()
  except ValueError:
    message = ("That is not a valid answer! Please choose a number from 1 to 4.")
    printMessage()

noLoopFlag = False

message = ("What club would you join if you had the chance? This definitely will not come up later.")
printMessage()
while questionAsking == 5:
  try:
    while noLoopFlag is False:
      message = ("Your options are...\n")
      printMessage()
      message = ("1. Theater\n")
      printMessage()
      message = ("2. Writing\n")
      printMessage()
      message = ("3. Art\n")
      printMessage()
      message = ("4. Photography")
      printMessage()
      message = ("5. Chess")
      printMessage()
      noLoopFlag = True
    Club = int(input(""))
    if Club == 1:
      Club = "theater"
      questionAsking = questionAsking + 1
    elif Club == 2:
      Club = "writing"
      questionAsking = questionAsking + 1
    elif Club == 3:
      Club = "art"
      questionAsking = questionAsking + 1
    elif Club == 4:
      Club = "photography"
      questionAsking = questionAsking + 1
    elif Club == 5:
      Club = "chess"
      questionAsking = questionAsking + 1
    else:
      message = ("Thats not a valid answer. Please choose a number from 1 to 5.")
      printMessage()
      
  except ValueError:
    message = ("That is not a valid answer! Please choose a number from 1 to 5.")
    printMessage()

noLoopFlag = False

message = ("What color is your favorite from this list? ")
printMessage()
while questionAsking == 6:
  try:
    while noLoopFlag is False:
      message = ("Your options are...\n")
      printMessage()
      message = ("1. Red\n")
      printMessage()
      message = ("2. Orange\n")
      printMessage()
      message = ("3. Yellow\n")
      printMessage()
      message = ("4. Green\n")
      printMessage()
      message = ("5. Blue\n")
      printMessage()
      message = ("6. Purple\n")
      printMessage()
      message = ("7. Pink\n")
      printMessage()
      message = ("8. Turquoise")
      printMessage()
      noLoopFlag = True
    Color = int(input(""))
    if Color == 1:
      Color = "red"
      questionAsking = questionAsking + 1
    elif Color == 2:
      Color = "orange"
      questionAsking = questionAsking + 1
    elif Color == 3:
      Color = "yellow"
      questionAsking = questionAsking + 1
    elif Color == 4:
      Color = "green"
      questionAsking = questionAsking + 1
    elif Color == 5:
      Color = "blue"
      questionAsking = questionAsking + 1
    elif Color == 6:
      Color = "purple"
      questionAsking = questionAsking + 1
    elif Color == 7:
      Color = "pink"
      questionAsking = questionAsking + 1
    elif Color == 8:
      Color = "turquoise"
      questionAsking = questionAsking + 1
    else:
      message = ("Thats not a valid answer. Please choose a number from 1 to 8.")
      printMessage()

  except ValueError:
    message = ("That is not a valid answer! Please choose a number from 1 to 8.")
    printMessage()
