#!/usr/bin/python3
# Christian Anderson
# 1/15/2020

'''a program to reset the pickle file associated with game_library.py'''

import pickle

games = {1:['FPS', 'Halo3', 'Bungee', 'Microsoft', 'Xbox', '2007', '10', 'either', '30.00', 'Yes', '1/15/2008', 'This game is overrated'],
         2:['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']}

datafile = open("game_library.pickle", "wb")
pickle.dump(games, datafile)
datafile.close()