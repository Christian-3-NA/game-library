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
        print("Title:        ", games[key][1], "\nGenre:        ", games[key][0], "\nDeveloper:    ", games[key][2], "\nPublisher:    ", games[key][3],
              "\nSystem:       ", games[key][4], "\nRelease Date: ", games[key][5], "\nRating:       ", games[key][6], "\n# of Players: ", games[key][7],
              "\nPrice:        ", games[key][8], "\nBeaten?:      ", games[key][9], "\nPurchase Date:", games[key][10], "\nNotes:        ", games[key][11])
        print("--------------")    
    
def search():

    def search_using(question, dict_position):
        found_one = False
        search_term = input(question)
        for key in games.keys():
            if search_term.lower() in (games[key][dict_position]).lower():
                found_one = True
                print()
                print("Title:        ", games[key][1], "\nGenre:        ", games[key][0], "\nDeveloper:    ", games[key][2], "\nPublisher:    ", games[key][3],
                      "\nSystem:       ", games[key][4], "\nRelease Date: ", games[key][5], "\nRating:       ", games[key][6], "\n# of Players: ", games[key][7],
                      "\nPrice:        ", games[key][8], "\nBeaten?:      ", games[key][9], "\nPurchase Date:", games[key][10], "\nNotes:        ", games[key][11])
                print("--------------")
        
        if not found_one:
            print("\n*** NO MATCHES FOUND!***")
            
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
    choice = input("Which term would you like to search? ")
    
    if choice == "1":
        search_using("  What is the title of the game? ", 1)

    elif choice == "2":
        search_using("  What is the genre of the game? ", 0)
         
    elif choice == "3":
        search_using("  Who is the developer of the game? ", 2)
        
    elif choice == "4":
        search_using("  Who is the publisher of the game? ", 3)
                  
    elif choice == "5":
        search_using("  What systems can the game play on? ", 4)
       
    elif choice == "6":
        search_using("  What is the release date of the game? ", 5)
            
    elif choice == "7":
        search_using("  What did you rate this game? ", 6)
        
    elif choice == "8":
        search_using("  How many players can play this game? ", 7)
       
    elif choice == "9":
        search_using("  What is the price of the game? ", 8)
                   
    elif choice == "10":
        search_using("  Have you beaten the game? ", 9)
            
    elif choice == "11":
        search_using("  What is the purchase date of the game? ", 10)
          
    else:
        print("\n*** THATS NOT AN OPTION! ***")
          

def add_or_edit():
    #print("Running add_or_edit()")
    add_edit_choice = input("  Would you like to edit an existing entry(1) or add a new one(2)? ")
    if add_edit_choice == "1":
        found_one = False
        valid = False
        print("    List of titles: ")
        for key in games.keys():
            print("     ", games[key][1])
        search_term = input("  What is the title of the game you wish to edit? ")
        for key in games.keys():
            if search_term.lower() == (games[key][1]).lower():
                found_one = True
                print("\n--------------")
                print("Genre:        ", games[key][0], "\nTitle:        ", games[key][1], "\nDeveloper:    ", games[key][2], "\nPublisher:    ", games[key][3],
                      "\nSystem:       ", games[key][4], "\nRelease Date: ", games[key][5], "\nRating:       ", games[key][6], "\n# of Players: ", games[key][7],
                      "\nPrice:        ", games[key][8], "\nBeaten?:      ", games[key][9], "\nPurchase Date:", games[key][10], "\nNotes:        ", games[key][11])
                print("--------------")
                while not valid:
                    part_to_edit = input("\nWhich part would you like to edit(1, 2, 3... 11, 12)? ")
                    new_part = input("\nWhat would you like the new part to be? ")
                    old_part = games[key][int(part_to_edit)-1]
                    games[key][int(part_to_edit)-1] = new_part
                    print("\n--------------")
                    print("Genre:        ", games[key][0], "\nTitle:        ", games[key][1], "\nDeveloper:    ", games[key][2], "\nPublisher:    ", games[key][3],
                          "\nSystem:       ", games[key][4], "\nRelease Date: ", games[key][5], "\nRating:       ", games[key][6], "\n# of Players: ", games[key][7],
                          "\nPrice:        ", games[key][8], "\nBeaten?:      ", games[key][9], "\nPurchase Date:", games[key][10], "\nNotes:        ", games[key][11])
                    print("--------------\n")
                    if (input("Type keep/k to confirm this change. ")).lower() not in ("keep", "k"):
                        games[key][int(part_to_edit)-1] = old_part
                    if (input("\nIs that everything? ")).lower() in ("yes", "y"):
                        valid = True
            
        if not found_one:
            print("\n***THAT GAME DOESN'T EXIST!***")        
        
    elif add_edit_choice == "2":
        new_key = len(games)+1
        new_entry = []
        valid = False
        while not valid:
            new_entry.append(input("What is the genre? "))
            new_entry.append(input("What is the title? "))
            new_entry.append(input("What is the developer? "))
            new_entry.append(input("What is the Publisher? "))
            new_entry.append(input("What are the systems? "))
            new_entry.append(input("What is the release year? "))
            new_entry.append(input("What is your rating? "))
            new_entry.append(input("What is the number of players? "))
            new_entry.append(input("What is the price? "))
            new_entry.append(input("Have you beaten it? "))
            new_entry.append(input("What is the purchase date? "))
            new_entry.append(input("Do you have any notes? "))
            print(new_entry)
            answer = input("Is this correct? ")
            if answer.lower() in ("yes", "y"):
                valid = True
            
            games[new_key] = new_entry
    else:
        print("\n*** THATS NOT AN OPTION! ***") 
    
def remove_game():
    #print("Running remove_game()")
    found_one = False
    delete_confirm = False
    print("  List of titles: ")
    for key in games.keys():
        print("     ", games[key][1])
    search_term = input("What is the title of the game you wish to delete? ")
    for key in games.keys():
        if search_term.lower() == (games[key][1]).lower():
            found_one = True
            print("\n--------------")
            print("Genre:        ", games[key][0], "\nTitle:        ", games[key][1], "\nDeveloper:    ", games[key][2], "\nPublisher:    ", games[key][3],
                  "\nSystem:       ", games[key][4], "\nRelease Date: ", games[key][5], "\nRating:       ", games[key][6], "\n# of Players: ", games[key][7],
                  "\nPrice:        ", games[key][8], "\nBeaten?:      ", games[key][9], "\nPurchase Date:", games[key][10], "\nNotes:        ", games[key][11])
            print("--------------")
            if (input("\nIs this the game you would like to delete? ")).lower() in ("yes", "y"):
                games.pop(key)
                break
              
    if not found_one:
        print("\n***THAT GAME DOESN'T EXIST!***") 
    
def save_changes():
    #print("Running save_changes()")
    datafile = open("game_library.pickle", "wb")
    pickle.dump(games, datafile)
    datafile.close()
    
    print("")
    print("Data Saved!")
    
def quit():
    if (input("  Would you like to save before quitting? ")).lower() in ("yes", "y"):
        datafile = open("game_library.pickle", "wb")
        pickle.dump(games, datafile)
        datafile.close()
        
        print("")
        print("Data Saved!")        
    print("\nGoodbye!")
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