import random
import os
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_card = []
comp_card = []
#########################

def deal(current_card):
    current_card.append(random.choice(cards))

def report(time):
    if time == "final":
        print(f"     Your cards: {user_card}, final score: {sum(user_card)}")
        print(f"     Computer's final card: {comp_card}, final score: {sum(comp_card)}")
    else:
        print(f"     Your cards: {user_card}, current score: {sum(user_card)}")
        print(f"     Computer's first card: {comp_card[0]}")

def judge():
    dif_user_card = 21 - sum(user_card)
    dif_comp_card = 21 - sum(comp_card)
    if(dif_user_card < 0 and dif_comp_card < 0):
        print("You both went over. Draw.")
    elif(dif_user_card < 0):
        print("You went over. You lose.")
    elif(dif_comp_card < 0):
        print("Opponent went over. You win.")
    elif(dif_user_card > dif_comp_card):
        print("You lose.")
    elif(dif_user_card < dif_comp_card):
        print("You win.")
    else:
        print("Draw")

def initial():
    os.system('clear')
    print(logo)
    global user_card, comp_card
    user_card = []
    comp_card = []
    for time in range(2):
        deal(user_card)
        deal(comp_card)
    report("current")
   
#########################
 
if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    is_play = True
else: 
    is_play = False
    
while(is_play):
    initial()
    
    #user
    while (sum(user_card) < 21 and
           (input("Type 'y' to get another card, type 'n' to pass: ") == "y")):
        deal(user_card)
        report("current")
    
    #computer
    while (21-sum(comp_card) > 6):
        deal(comp_card)
    
    #judge
    report("final")
    judge()
    is_play = (input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y")
        
    
    
        
    
    
    
    
    
    

    

