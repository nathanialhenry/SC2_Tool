# SC2_Tool

This Repo contains the following Scripts:

sc2Parse.py - command line tool that uses the sc2reader library to parse Starcraft Replays and display either per match or aggregate data from the replay folder.
	requires command line arguments for --path (filepath to starcraft replays), and -a (selected if you want match specific data in the output)
sc2ParseandGui.py - the sc2Parse.py tool wrapped in TK GUI (WIP)

Both scripts require sc2reader library and the sc2ParseandGui.py script requires tkinter as well (see Requirments.txt)

