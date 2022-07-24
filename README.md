![](https://github.com/rrsolomon/Steam-Build-ID-Finder/blob/main/Assets/Steam%20Build%20ID%20Finder%20Banner.PNG)

Simple Python script that pulls the name, and build-ID of games from .acf files.

# Pre-Requisites
- **Python** | https://www.python.org/downloads/

# How to Use
1. **Place the Steam Build ID Finder on your desktop.**

2. **Set the steamapps directory.** Open up the Python script in some text editor, and make sure to change the `path` variable to the directory that you `steamapps` folder is located. Normally this is located in the `C:\Program Files\Steam\steamapps`. The script will scan all of your `.acf` files and bring back the Game Title, Steam Build ID for said game, and the `.acf` file that is associated with that game.

3. **Run `python Steam BuildID Finder.py >> Build_IDs.txt`**. This will export the results into a file neatly on to your desktop. You don't need to do this step. You can simply view the results on a terminal, but it helps for quick reference if that's something you're interested in.

# Other Notes
The build-ID can be found on `line 12` inside your `.acf` file and the name of the game can be found on `line 6`.

![](https://github.com/rrsolomon/Steam-Build-ID-Finder/blob/main/Assets/acf%20file%20info.PNG)
