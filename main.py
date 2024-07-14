from os import system, name
import random


logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
        
def ask():
    answer=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if answer=='n':
        clear()
        ask()
    elif answer=='y':
        clear()
        print(logo)
        list_of_cards=['11', '2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10']
        my_cards=random.sample(list_of_cards, 2)
        
        
        sum=0
        for i in range(0, 2):
            sum+=int(my_cards[i])
            i+=1
            
        comp_card=random.sample(list_of_cards, 2)
        
    
        sum1=0
        for i in range(0, 2):
            sum1+=int(comp_card[i])
            i+=1
        
        print(f"Your cards: {my_cards}, current score: {sum}\nComputer's first card: {comp_card[0]}" )
        
        answer2=input("Type 'y' to get another card, type 'n' to pass: ")
        if answer2=='n':
            print(f"Your final hand: {my_cards}, final score: {sum}\nComputer's final card: {comp_card}, final score: {sum1}" )
            if sum>sum1 and sum<=21 and sum1>=17:
                print("You Win!!!\n")
            elif sum1<17:
                comp_card+=random.sample(list_of_cards, 1)
                sum1+=int(comp_card[2])
                print(f"Oh! It was less than 17 so Computer's final card: {comp_card}, final score: {sum1}\n")
                if sum1<17:
                    comp_card+=random.sample(list_of_cards, 1)
                    sum1+=int(comp_card[2])
                    print(f"Oh! It was less than 17 so Computer's final card: {comp_card}, final score: {sum1}\n")
                    if sum1>21:
                        print("You Win!!!!!!!!\n")
                    elif sum>sum1 and sum<=21:
                        print("You Win!!!!\n")
                    elif sum==sum1 and sum<=21:
                        print("It's a draw!\n")
                    elif sum<sum1 or sum>21:
                        print("You lose!!!!!\n")
                
                else:
                    if sum1>21:
                        print("You Win!!!!!!!!\n")
                    elif sum>sum1 and sum<=21:
                        print("You Win!!!!\n")
                    elif sum==sum1 and sum<=21:
                        print("It's a draw!\n")
                    elif sum<sum1 or sum>21:
                        print("You lose!!!!!\n")
                    
            elif sum1>21:
                print("You Win!!!!!\n")
            elif sum>21:
                print("You went over. You lose!!!!\n")
            elif sum<sum1 and sum<=21 and sum1>=17:
                print("You lose!!!!!!\n")
            elif sum==sum1:
                print("It's  a draw!!!\n")
            ask()    
            
        elif answer2=='y':
            my_cards+=random.sample(list_of_cards, 1)
            sum+=int(my_cards[2])
            print(f"Your final hand: {my_cards}, final score: {sum}\nComputer's final card: {comp_card}, final score: {sum1}" )
            if sum>21:
                print("You went over. You lose!!!!\n")
            elif sum>sum1 and sum<=21 and sum1>=17:
                print("You Win!!!\n")
            elif sum1<17:
                comp_card+=random.sample(list_of_cards, 1)
                sum1+=int(comp_card[2])
                print(f"Oh! It was less than 17 so Computer's final card: {comp_card}, final score: {sum1}\n")
                if sum1<17:
                    comp_card+=random.sample(list_of_cards, 1)
                    sum1+=int(comp_card[2])
                    print(f"Oh! It was less than 17 so Computer's final card: {comp_card}, final score: {sum1}\n")
                    if sum1>21:
                        print("You Win!!!!!!!!\n")
                    elif sum>sum1 and sum<=21:
                        print("You Win!!!!\n")
                    elif sum==sum1 and sum<=21:
                        print("It's a draw!\n")
                    elif sum<sum1 or sum>21:
                        print("You lose!!!!!\n")
                
                else:
                    if sum1>21:
                        print("You Win!!!!!!!!\n")
                    elif sum>sum1 and sum<=21:
                        print("You Win!!!!\n")
                    elif sum==sum1 and sum<=21:
                        print("It's a draw!\n")
                    elif sum<sum1 or sum>21:
                        print("You lose!!!!!\n")
                    
                    
            elif sum1>21:
                print("You Win!!!!!\n")
            
            elif sum<sum1 and sum<=21 and sum1>=17:
                print("You lose!!!!!!\n")
            elif sum==sum1:
                print("It's  a draw!!!\n")
            ask()

ask()
