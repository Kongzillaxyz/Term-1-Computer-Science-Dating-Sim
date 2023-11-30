AskSomeoneAge = False
Setting = None
Range = None
Club = None
Shop = None
Relationship1 = 0
Relationship2 = 0
Relationship3 = 0


#Setting the first interaction variable
Alt1 = None
Main = None
Alt2 = None
Question1 = None
Question2 = None
Alt2Choice = False
Knives = False
AsheRelations = False
AsheHate = False
RoseRelations = False
#Project Variable for School
Project = None


#Character specific
#Set Variables Here

import random
#Importing the random generator

#Opening Code
print("Hello Player! Welcome to Love Through the Odds!")
#Fix the name later please
PlayerName = input("What is your name? ")

print("Wonderful,", PlayerName + "!")
#Now we need characters

#Women: Daria, Ashe, Rose
#Personality Daria: Extroverted, Loud, Creative
#Personality Ashe: Sassy, Daring, Curious
#Personality Rose: Smart, Obsessive, Touchy

#Men: Nathan, Xavier, Jade, Liam
#Personality Nathan: Depressed, Caring, Collects Knives
#Personality: Jade: Flamboyant, Hard Working, Arrogant
#Personality: Liam: Sweet, Smooth, Selfish

#Nonbinary: Crow
#Personality Crow: Sarcastic, Accidentally Destructive, Amusing

#Lists to randomise the order generated
Women = ["Daria", "Ashe", "Rose"]
#Women ListWo
Men = ["Nathan", "Jade", "Liam"]
#Men List
Nonbinary = ["Crow"]
#Nonbinary List

#Survery
print("Now we have a short survery to improve your game experience!")
#Preference to Select from lists and allows player to have a more diverse experience.
PreferenceTry = True
while PreferenceTry == True:
  try:
    Preference = input("What is your gender preference? Please enter 'men' 'women' or 'none': ")
    if Preference == "women":
      WomenChoice = random.sample(Women, 3)
      Woman1 = WomenChoice[0]
      Woman2 = WomenChoice[1]
      Woman3 = WomenChoice[2]
      PreferenceTry = False
    elif Preference == "men":
      MenChoice = random.sample(Men, 3)
      Man1 = MenChoice[0]
      Man2 = MenChoice[1]
      Man3 = MenChoice[2]
      PreferenceTry = False
    elif Preference == "none":
      Woman1 = random.choice(Women)
      Man1 = random.choice(Men)
      Non1 = random.choice(Nonbinary)
      PreferenceTry = False
    else:
      print("I don't understand. Please try again!")
  except ValueError:
     print("What???")
print("Amazing!")

#This next section is to check what characters are currently in the code to influence actions and interactions. This builds more believable characters.

#This is to get your age then give you a funny response and give you setting
AskSomeoneAge = True
while AskSomeoneAge == True:
  try:
    Age = int(input("How old are you? "))
    if Age < 13:
      print("You are not old enough to date! Also you should not be playing this game. Please lie next time!")
    elif Age > 18:
      print("Too bad! You're in High School again! Welcome back to 16 years old!")
      AskSomeoneAge = False
    elif Age < 16:
      print("Happy Birthday because you're 16 now! Enjoy your new found age!")
      AskSomeoneAge = False
    elif Age == 17 or Age == 18:
      print("You're 16 again! Amazing! The other years must have been a dream!")
      AskSomeoneAge = False
    else:
      AskSomeoneAge = False
      print("Amazing!")
  except ValueError:
    print("That is not a valid age! Please try again!")

#These questions may be used later on to influence personality
Color = input("What's your favorite color? ")
print("Awesome!")
Food = input("What's your favorite food? ")
print("Amazing!")
Hair = input("What's your hair color? ")
print("Love it!")
Eyes = input("What's your eye color? ")
print("Beautiful!")
print("What's your Social Security--10101--- I'm sorry! Wrong code!")
Hobby = input("What's your hobby? ")
#Checks what the setting is to see if it needs to ask this question.
ChooseClub = True

#This format prevent invalid answers from being entered. This prevents the code from breaking
#This gives you a basic setting.
while ChooseClub == True:
  try:
    Club = input("Sounds like you're in High School! We have a few different club options for you so please choose one of the following: chess, drama, art, technology, writing, dnd, or photography. ")
    if Club == "chess":
      Project = "PlayChess"
      ChooseClub = False
    elif Club == "drama":
      Project = "PracticScript"
      ChooseClub = False
    elif Club == "art":
      Project = "DrawTogether"
      ChooseClub = False
    elif Club == "technology":
      Project = "RoboticsProject"
      ChooseClub = False
    elif Club == "writing":
      Project = "StoryTogether"
      ChooseClub = False
    elif Club == "dnd":
      Project = "TeachGame"
      ChooseClub = False
    elif Club == "photography":
      Project = "PhotosOfPerson"
      ChooseClub = False
    else:
      print("I don't understand. Please try again!")
  except ValueError:
     print("What???")

#The Projects are set for later additions of activities to do
#Quiz Questions Continued
#Fix the easy breakabilty


#School Section
if Preference == "women":
  print("It's Monday after school and you are heading to", Club + " club. The other club members are",Woman1+",",Woman2+", and",Woman3+".")
elif Preference == "men":
  print("It's Monday after school and you are heading to", Club + " club. The other club members are",Man1+",",Man2+", and",Man3+".")
elif Preference == "none":
  print("It's Monday after school and you are heading to", Club + " club. The other club members are",Woman1+",",Man1+", and",Non1+".")

  print("You are new to this club and know very little about any of your fellow members. Still, you have to choose who'd you'd like to spend your time with as a bit of club bonding.")

if Preference == "women":
  print("As stated before the club members are", Woman1+",",Woman2+", and", Woman3+".")
elif Preference == "men":
  print("As stated before the club members are", Man1+",",Man2+", and", Man3+".")
elif Preference == "none":
  print("As stated before the club members are", Woman1+",",Man1+", and", Non1+".")


ChooseChoice = True

while ChooseChoice == True:
  try:
    Choice1 = input("Who would you like to talk to?  ")
    if Preference == "women" or Preference == "men" or Preference == "none":
      
      if Choice1 == "Rose":
        print("She seems happy to talk to you. She takes your arm as you two walk.")
        ChooseChoice = False
      elif Choice1 == "Daria":
        print("Daria beems at you and immediately starts chatting. 'I'm glad you wanted to talk. You seem so interesting!'")
        ChooseChoice = False
      elif Choice1 == "Ashe":
        print("She nods and walks next to you. 'Not everyday someone wants to talk to me. You may have some guts after all.'")
        ChooseChoice = False
        #Now the men
      
      elif Choice1 == "Nathan":
         print("He was frowning. The expression was almost glued to his face. But still he walks with you.")
         ChooseChoice = False
      elif Choice1 == "Jade":
        print("He steps forward and walks next to you. 'I'm Jade. Nice to meet you. Love the style, almost as good as mine.'")
        ChooseChoice = False
      elif Choice1 == "Liam":
        print("He starts walking next to you. 'I'm Liam. I'm glad I get to talk to you.'")
        ChooseChoice = False
        
        #The Nonbinary
      elif Choice1 == "Crow":
       print("They chuckle and walk up to you. 'Choose me because I'm such a ray of sunshine?' They make a gesture to indicate the sun in the sky.")
       ChooseChoice = False
        
      else:
       print("I don't understand. Make sure you entered 1, 2, or 3.")

  except ValueError:
     print("Please try again.")




#Breaking up for each gender to keep it easy



#STORY AHHHHH set to each specific character for personality reasons

  print("Now it's time for your first choice! There will be listed options of 1, 2, or 3. You input the option you'd like to choose! These choices will effect different aspects of your story but let's start with an easy one to get you going!")


SitCheck = True

while SitCheck == True:
  try:
    Sit = int(input("You see three main places you could sit to talk! 1: A table in the room with two chairs. 2: A carpetted corner of the room. 3: Go outside and sit in the sun. Where would you like to sit?  "))
    if Sit == 1:
      print("You two sit down at the table.")
      SitCheck = False
    elif Sit == 2:
      print("You sit in the corner of the room.")
      SitCheck = False
    elif Sit == 3:
      print("You sit outside in the Sun. It is nice and warm.")
      SitCheck = False
    else:
      print("I don't understand. Make sure you entered 1, 2, or 3.")

  except ValueError:
    print("Please try again.")

print("Time for your next choice! You need to start a conversation!")

Conversation = True

while Conversation == True:
  try:
    Talk = int(input("Now its time for some real decision making! This next choice will effect how this character perceives you 1: Introduce yourself politely. 2: Stay silent. 3: Ask questions."))
    if Talk == 1:
      print("'Hi. I'm",PlayerName+". I'm 16 years old.")
      Main = True
      Conversation = False
    elif Talk == 2:
      Alt1 = True
      Conversation = False
    elif Talk == 3:
      print("'How old are you?'")
      Alt2 = True
      Conversation = False
      Alt2Choice = True
    else:
      print("I don't understand. Make sure you entered 1, 2, or 3.")

  except ValueError:
    print("Please try again.")

#Silence Option. Certain Characters have unique sayings to add some variance to the game
if Alt1 == True and Choice1 == "Rose":
  print("'You're very quiet. I suppose that's nice. Maybe you're a deep thinker? Hmm... what's going on in your head...' she stares at you long enough for it to get a bit uncomfortable.")
elif Alt1 == True and Choice1 == "Ashe":
  print("'So silence? Ugh. I thought you'd actually talk.' She seems annoyed with you.")
  print("Oh no! You've come up to effecting your Relationship Levels! Currently your Relationship level with Ashe is neutral. If you bring it down to Hate you can't date her! She has standards! If you think Ashe is the person you like you better make her happy!")
  AsheRelations = True
elif Alt1 == True and Choice1 == "Daria":
  print("Daria doesn't seem to like the silence and starts talking about her art projects she's done.")
elif Alt1 == True and Choice1 == "Nathan":
  print("You two sit in silence for some time before Nathan pulls a knife out of his pocket. He starts fiddling with it.")
  print("Wow! Your choices led to a bonus option! These are avaliable through the game to possibly provide extra time for you to speak with the characters and learn more about them!")
  Knives = True
elif Alt1 == True and Choice1 == "Crow":
  print("'Well don't you just talk someone's ear off.' They sigh and stares at you.")
elif Alt1 == True and Choice1 == "Liam" or Choice1 == "Jade":
  print("You sit in an awkward silence.")

if Alt2 == True:
  print("'I'm 16."'')
  print("Ooo this choice is fun. You get to ask a few of your own questions. Choose from these pre-made questions!")
  Alt2Choice = True

#The Main choice code for if you choose to talk to the person. This has more indivudual actions
if Main == True and Choice1 == "Crow":
  print("'I'm Crow. Before you ask, no. Crow is not my birth name but that's what you can call me.' They look at you unamused.")
elif Main == True and Choice1 == "Rose":
  print("'I'm Rose! I'm 16 too!''")
  print("'Uh my favorite color is-'")
  print("She cuts you off. 'It's", Color+" right? My favorite too! My favorite food is", Food+"! You enjoy that don't you? Sorry I'm being forward. We're so similar though!'")
  #Explaination of Relationship level here
  print("You've come up to effecting your Relationship Levels! Currently your Relationship level with Rose is Neutral. Bringing it up to Like gives you the option to date her! Don't make her mad. If you think Rose is the person you like you better make her happy!")
  RoseRelations = True
elif Main == True and Choice1 == "Daria":
  print("She smiles. 'I'm Daria. Nice to meet you! I just love art and drawing. It's my passion! What do you like to do in your freetime?''")
  print("Your quiz answers did matter! 'I enjoy", Hobby+".' She studies you for a second. 'Interesting answer.' She responds.")
elif Main == True and Choice1 == "Ashe":
  print("'My name is Ashe. I'm curious why you talked to me. I like it though. I'm glad we're chatting.'")
elif Main == True and Choice1 == "Nathan":
  print("'Nathan. I'm a collector of sorts.' He seems distant in the conversation.")
elif Main == True and Choice1 == "Jade":
  print("'Interesting. I'm 16 too. You're pretty cool.'")
elif Main == True and Choice1 == "Liam":
  print ("'Oh cool. I'm 16 too. I'm a fan of the", Eyes+" eyes. They're very cool.")

#Each Ending was done but not Creativily filled in

#If you used Alt2 you now get to ask questions
  
while Alt2Choice == True:
      Questions = int(input("Now its time for some real decision making! This next choice will effect how this character perceives you 1: How would you describe yourself in one word? 2: Do you like me?"))
      if Questions == 1:
        Question1 = True
        Alt2Choice = False
      elif Questions == 2:
        Question2 = True
        Alt2Choice = False
      else:
        print("I don't understand. Make sure you entered 1, 2, or 3.")


#List might be good to add some spiced up responses
if Question1 == True:
  if Choice1 == "Daria":
    print("'Artsy!' She states quite loudly.")
  elif Choice1 == "Ashe":
    print("'Bold. Just like you're being with these questions.' She chuckles.'")
  elif Choice1 == "Rose":
    print("'Uhh... hmm... one word? Oh! How about determined? That sounds good.'")
  elif Choice1 == "Nathan":
    print("'Collector.' He looks at you. 'Have I told you I collect knives? They are quite cool. Nevermind. I'll tell you about it later.")
  elif Choice1 == "Jade":
    print("'Amazing. Easy question.' He flashes a smile.")
  elif Choice1 == "Liam":
    print("'I suppose I'd call myself sweet. I'm a good spirit.' He smiles.")
  elif Choice1 == "Crow":
    print("'Sunny.' She chuckles. 'Maybe problematic.' She shrugs. 'I'm just being sarcastic. Maybe I'd describe myself as eractic.'")

#Throwing in a list to add randomness and reduce the amount of unnecessary responses
FunResponses1 = ["'Yeah. You're nice. A cool person.''", "'I'm warming up to you. This conversation is helping.'", "'Uh sure. I guess.'"]
FunResponses2 = ["'Should I?'", "'I don't have much to go off of so I can't say.'", "'We'll see.'"]

if Question2 == True:
  if Choice1 == "Daria" or Choice1 == "Rose" or Choice1 == "Nathan" or Choice1 == "Jade" or Choice1 == "Liam":
    Response = random.choice(FunResponses1)
  elif Choice1 == "Ashe" or Choice1 == "Crow":
    Response = random.choice(FunResponses2)
  print(Response)

while Knives == True:
  KnifeAnswer = int(input("You get to ask one of 2 questions. Choose wisely! 1: Why do you have a knife? 2: Do you like knives?"))
  if KnifeAnswer == 1:
    print("'I like collecting them. They are really cool. I've got a whole wall of them back home.'")
    Knives = False
  elif KnifeAnswer == 2:
    print("'I love them! Got a whole collection.'")
    Knives = False
  else:
    print("I don't understand. Make sure you entered 1, 2, or 3.")

while AsheRelations == True:
  AsheEntertain = int(input("You've got 2 options. 1: Stay Silent. 2: Talk."))
  if AsheEntertain == 1:
    print("'Ugh. Nevermind. Don't talk to me again.' Oh no! You've lost Relations with this character! This character is no longer an option to date.")
    AsheHate = True
  elif AsheEntertain == 2:
    print("You two have a basic conversation. She doesn't hate you. Nice!")

while RoseRelations == True:
  RoseEntertain = int(input("You've got 2 options. 1: 'You're right. We are similar. It's great to talk to you.' 2: 'We aren't similar and you're creepy! I don't like you.'"))
  if RoseEntertain == 1:
    print("'I knew it! We are similar! You're so cool!' Great job! Rose likes you!")
  elif RoseEntertain == 2:
    print("'What?' She stares at you then gets up and leaves. You end up talking to the other members of the club and they both Like you! Amazing!")
    print("You head home and spend some time",Hobby+". You soon head to bed and fall asleep.")
    print("'I used to like you.' That voice wasn't your own but felt familar. 'I followed you. Watched you. Learned about you. I thought you were cool but now... I realize the truth. You hurt me. So now you'll feel that pain a thousand times over... goodbye. I love you... no more.' You're body goes cold.")
    print("Congratulation! You're dead!")
    Dead = True
    exit()


print("Soon your talk comes to an end and the club gets on with its normal activities.")

