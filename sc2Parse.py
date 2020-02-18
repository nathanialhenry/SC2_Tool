
import argparse
import sc2reader
import os

# Allow this script to take a filepath, and per match stats as an input
parser = argparse.ArgumentParser(description="Parses a filepath for the replay viewer")
parser.add_argument("--path", type=str, help="Full Filepath to the starcraft replays")
parser.add_argument("-a", action = "count", help="Select if you want match specific data per replay")

args = parser.parse_args()

match_replays = os.listdir(args.path)
listall = args.a
full_paths = []

# Build a list of full filepaths to replays
for item in match_replays:
    full_paths.append(os.path.join(args.path, item))

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
# Print results to console if -a
        if listall:
            print("MAP: {0}".format(replay_map))
            print("LENGTH: {0}".format(replay_length))
            print("TEAMS: {0}".format(replay_teams))
            print("DATE: {0}".format(replay_date))
            print("-----------------------------------------")
        else:
            continue
    except Exception as e:
        print("Exception occurred at {0}".format(e))
print("========================================================================")
average_length = length_sum / file_counter
print("AVERAGE GAME TIME: {0} Minutes".format(round(average_length / 60 , 0)))
