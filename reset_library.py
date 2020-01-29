#!/usr/bin/python3
# Christian Anderson
# 1/15/2020

'''a program to reset the pickle file associated with game_library.py'''

import pickle

games = {1:['FPS', 'Halo3', 'Bungie', 'Microsoft', 'Xbox', '2007', '10', '1-2', '30.00', 'Yes', '1/15/2008', 'This game is overrated'],
         2:['RPG', 'Undertale', 'Toby Fox', '8-4', 'PC, PS4, PS Vita, Nintendo Switch', '2015', '10', '1', '10.00', 'Yes', '2/2/2016', 'Its pretty darn good yo'],
         3:['FPS', 'Team Fortress 2', 'Valve', 'Valve', 'PC, Xbox', '2007', '8', '1', 'Free', 'N/A', '4/7/2013', 'Hard to get good at'],
         4:['Sandbox', 'Minecraft', 'Mojang', 'Mojang', 'PC, PS4, Xbox, Nintendo Switch, Mobile', '2009', '10', '1-4', '27.00', 'Yes', '3/7/2022', 'Something for everyone']}

datafile = open("game_library.pickle", "wb")
pickle.dump(games, datafile)
datafile.close()