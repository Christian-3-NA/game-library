#!/usr/bin/python3
# Christian Anderson
# 1/27/2020

'''A database to store video games with various tags'''

import pickle

def print_all():
    #print("Running print_all()")
    key_list = games.keys()
    
    for key in key_list:
        print()
        print("Title:", games[key][1], "   Genre:", games[key][0], "   Developer:", games[key][2], "   Publisher:", games[key][3])
        print("System:", games[key][4], "   Release Date:", games[key][5], "   Rating:", games[key][6], "   Number of Players:", games[key][7])
        print("Price:", games[key][8], "   Beaten?:", games[key][9], "   Purchase Date:", games[key][10], "   Notes:", games[key][11])
        print("----------------------")    
    
def search():
    print("""
    What would you like to search by?
    ---------------------------------
    
    SEARCH BY:
    1) Title
    2) Genre
    3) Developer
    4) Publisher
    5) System
    6) Release Date
    7) Rating
    8) Number of Players
    9) Price
    10) Beaten?
    11) Purchase Date
    
    """)
    
def add_or_edit():
    print("Running add_or_edit()")
    
def remove_game():
    print("Running remove_game()")
    
def save_changes():
    #print("Running save_changes()")
    datafile = open("game_library.pickle", "wb")
    pickle.dump(games, datafile)
    datafile.close()
    
    print("")
    print("Data Saved!")
    
def quit():
    print("Goodbye!")
    exit()

games = {}
picklefile = open("game_library.pickle", "rb")
games = pickle.load(picklefile)
picklefile.close()

keep_going = True

while keep_going:
    print("""
    Greetings, gamer! Welcome to the library!
    -----------------------------------------
    
    MAIN MENU
    1) Print All Games
    2) Search Using Specification
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
    input("-----Press Enter to continue.-----")
        
print("Uh-Oh! Looks like both monkeys are smiling!")