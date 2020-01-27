#!/usr/bin/python3
# Christian Anderson
# 1/27/2020

'''A database to store video games with various tags'''

import pickle



games = {1:['FPS', 'Halo3', 'Bungee', 'Microsoft', 'Xbox', '2007', '10', 'either', '30.00', 'Yes', '1/15/2008', 'This is is overrated'],
         2:['3']}

def print_all():
    print("Running print_all()")
    
def search():
    print("""
    What would you like to search by?
    ---------------------------------
    
    SEARCH BY:
    1) Title
    2) Genre
    3) Developer
    4) Publisher
    etc...
    """)
    
def add_or_edit():
    print("Running add_or_edit()")
    
def remove_game():
    print("Running remove_game()")
    
def save_changes():
    print("Running save_changes()")
    
def quit():
    print("Goodbye!")
    exit()

keep_going = True

while keep_going:
    print("""
    Greetings, gamer! Welcome to the library!
    -----------------------------------------
    
    MAIN MENU
    1) Print All Games
    2) Search by ___
    3) Add/Edit Game
    4) Remove a Game
    5) Save Data 

    Q) Quit
    
    """)
    choice = input("What would you like to do? ")
    
    if choice == "1":
        print_all()
    elif choice == "2":
        search()
    elif choice == "3":
        add_or_edit()
    elif choice == "4":
        remove_game()
    elif choice == "5":
        save_changes() 
        
    elif choice == "Q" or choice == "q":
        quit()
    else:
        print("*** THATS NOT A COMMAND! ***")
    
    print("")
    input("Press Enter to continue.")
        
print("Uh-Oh! Looks like both monkeys are smiling!")