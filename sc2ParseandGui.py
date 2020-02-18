# TODO make listall radio button a counter/add 1 to variables
# make file path/directory work
# figure out how to reference/open sc2.txt in the textbox

import tkinter as tk
from tkinter import filedialog, Text
import os
import sc2reader


# create root object variable
root = tk.Tk()

# create title
root.title("SC2 Replay")
# lock window size
root.resizable(width=False, height=False)

# create window size and background color
canvas = tk.Canvas(root, height = 700, width = 700, bg="#263D42")
canvas.pack()

# create other color frame
frame = tk.Frame(root, bg = "white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# create text box for arguments
tk.Label(root, text="SC2Replays Folder Path:").place(relx=0.17, rely=0.918)
pathInput = tk.Entry(root)
pathString = str(pathInput)
# pathString = '/home/nathan/Downloads/multiplayer/' created this path for testing purposes
pathInput.pack(padx = 9, pady = 9)

# create the "all" option radio button
listall = 0

tk.Radiobutton(root,
              text="Per Match Info",
              padx = 20,
              variable= listall,
              value=1).place(relx = .61, rely = .918)

createFile= open('sc2.txt', 'w')
createFile.close()

# create run SC script button
def sc2Script(input_path):
    # Allow this script to take a filepath, and per match stats as an input

    print(input_path) # This input_path should be populated - if not, there's a bug

    match_replays = os.listdir(input_path)
    full_paths = []
    f = open('sc2.txt', 'w')

    # Build a list of full filepaths to replays
    for item in match_replays:
        full_paths.append(os.path.join(input_path, item))

    replays = sc2reader.load_replays(full_paths, load_level=4)
    length_sum = 0

    # Iterate through the replay files using date,time,length,and team methods
    # Enumerated replays for indexing for the file_counter
    # Using try except to avoid corrupt/<4 byte files breaking script
    for i, replayfile in enumerate(replays):

        try:
            replay_length = replayfile.length.seconds
            replay_map = replayfile.map_name
            replay_date = replayfile.date
            replay_teams = replayfile.teams
            length_sum += replay_length
            file_counter = i + 1
    # f.write results to console if -a
            if listall:
                f.write("MAP: {0}".format(replay_map))
                f.write("LENGTH: {0}".format(replay_length))
                f.write("TEAMS: {0}".format(replay_teams))
                f.write("DATE: {0}".format(replay_date))
                f.write("-----------------------------------------")
            else:
                continue
        except Exception as e:
            f.write("Exception occurred at {0}".format(e))
    f.write("========================================================================")
    average_length = length_sum / file_counter
    f.write("AVERAGE GAME TIME: {0} Minutes".format(round(average_length / 60 , 0)))


# sc2Button that Runs the sc2Script function
print(pathString) # Printing the pathString shows that the bottom textbox isn't receiving input
runScript = tk.Button(root, text="Run SC2 Script", padx = 8, pady = 8, fg="white", bg="#263D42", command= lambda:sc2Script(pathString) )
runScript.pack()


# reference sc2.txt to display window
scrollBar = tk.Scrollbar(root)
textbox = tk.Text(root)

textbox.focus_set()
scrollBar.place(relx=0.9, rely=0.2)
textbox.place(relx=0.1, rely=0.1,relwidth=0.8, relheight=0.8)
scrollBar.config(command=textbox.yview)
textbox.config(yscrollcommand=scrollBar.set)

displayText = open('sc2.txt', 'r')

# Try printing this readFile
readFile = displayText.read()

# According to the tk.text documentation, first arg is row.column
textbox.insert(1.0, readFile)
textbox.see(1.0)

# run script
root.mainloop()
