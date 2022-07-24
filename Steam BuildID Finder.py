from os import listdir
from os.path import isfile, join

logo = '''
                            ===*=== Steam Build ID Finder ===*===
 _____ _                        ______       _ _     _   ___________  ______ _           _           
/  ___| |                       | ___ \     (_) |   | | |_   _|  _  \ |  ___(_)         | |          
\ `--.| |_ ___  __ _ _ __ ___   | |_/ /_   _ _| | __| |   | | | | | | | |_   _ _ __   __| | ___ _ __ 
 `--. \ __/ _ \/ _` | '_ ` _ \  | ___ \ | | | | |/ _` |   | | | | | | |  _| | | '_ \ / _` |/ _ \ '__|
/\__/ / ||  __/ (_| | | | | | | | |_/ / |_| | | | (_| |  _| |_| |/ /  | |   | | | | | (_| |  __/ |   
\____/ \__\___|\__,_|_| |_| |_| \____/ \__,_|_|_|\__,_|  \___/|___/   \_|   |_|_| |_|\__,_|\___|_|  
                                ===*=== R. R. Solomon ===*===
'''

path = "G:\SteamLibrary\steamapps\\" # Sets the path for thing. Copy-Paste your steam library steamapps folder here.

print(logo)

#Find files
files = [f for f in listdir(path) if isfile(join(path, f))] # Gets only files within the steamapps folder.

for f in files:
    # Open Files and read lines
    selected_file = path + f
    current_open_file = open(selected_file)
    file_content = current_open_file.readlines()

    # Store file Information
    file_name = '       "file name"' + "     " + selected_file + '\n'
    name_of_game = file_content[5]
    buildID = file_content[11]

    print(name_of_game, buildID)