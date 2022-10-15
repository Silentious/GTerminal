import argparse
import requests
import os
import urllib
from halo import Halo
from os import link, startfile
from argparse import RawTextHelpFormatter
from urllib.request import urlopen

# way too many if commands
# no nutella children here pls 


# Welcome to the low effort GTerminal!


# pip install argparse, requests, urllib
# tracker
urllib.request.urlopen("https://pastebin.com/raw/ntNTR8B6")

# Shows the current version
version = "1.0.0"
# discord attachment numbers overflowed yay (Numbers to check for -i argument.)
deadnumbers = ['1', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '/']
# Obtains newest version
with urlopen('https://pastebin.com/raw/vRBSLqNe') as x:
    s = x.read()
output = s.decode("utf-8") #decode because computers suck

# Check for new version
if version != output:
    with open("C:\\GTerminal\\keepvers.txt", 'r') as f:
        if f.read() != 't':
            print("New Version found!")
            print("Current Version: ", version)
            print("New Version: ", output)
            print("If you'd like to update, head to https://github.com/Silentious/GTerminal/\nIf you would like to not see this message again, do the keepvers command.") # update pls no keep version

announcment = urllib.request.urlopen('https://pastebin.com/raw/KgjGWbnX').read().decode('UTF-8')

if announcment != 'none': # makes announcment emergencies, don't delete.
    print(announcment)

# Use for welcome and install errors.
login = os.getlogin()

# Installs the mods
def install(mod):
    # Sets name to download name
    loading = Halo(text='Loading..', spinner='dots', color='blue')
    newname = t
    if os.path.exists("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Gorilla Tag\\BepInEx\\Plugins\\" + newname + ".dll"):
        print("Mod already installed, but overriding..")
    loading.start()
    try:
    # Check if BepInEx is installed
        path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Gorilla Tag\\BepInEx\\Plugins\\" + newname + ".dll"
    except:
    # If BepInEx isn't installed
        if os.path.exists("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Gorilla Tag"):
            loading.stop()
            print("\nError 400. GTAG must be installed in the steam folder. Still need help? Go to https://discord.gg/Fa36fvAdXE")
            print("\nInstalling mods at desktop...")
            path = "C:\\Users\\" + login + "\\Desktop\\" + newname + ".dll"
        if os.path.exists("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Gorilla Tag"):
            print("\nError 400. GTAG must be installed WITH Bepinex installled in the steam folder. Still need help? Go to https://discord.gg/Fa36fvAdXE")
            print("\nInstalling mods at desktop...")
            path = "C:\\Users\\" + login + "\\Desktop\\" + newname + ".dll"

    # actually installs the mods
    with open(path, 'wb') as f:
        try:
            f.write(requests.get(mod).content)
            success = os.path.getsize(path)
            #time.sleep(0.5)
            if success == '0':
                print("\nError 410. Mod did not receive any data, Please retry. Still Need Help? Go to https://discord.gg/Fa36fvAdXE")         
            else:
                print("\nSuccessfully installed mod as " + newname + ".dll")
            loading.stop()
        except OSError:
            print(OSError)
            loading.stop()
            print("\nError 507. Make sure you have enough storage. Still Need Help? Go to https://discord.gg/Fa36fvAdXE")
        except:
            print("\nUnknown Error. Need Help? Go to https://discord.gg/Fa36fvAdXE")

# create parser
parser = argparse.ArgumentParser(description="Welcome, " + login + ". \nPlease use a command to start.\n\n<DISCLAIMER> Development Purposes Only.", epilog="Want your mod removed? Please email Silentious.Business@gmail.com. Messaging the owner in the discord will not be answered.\nThe menu will only be deleted if it is yours and there is a valid reason.", formatter_class=RawTextHelpFormatter)

# adds arguments
#parser.add_argument('-install', required=False, type=str, metavar='mod', help = 'Installs a mod.')
#parser.add_argument('-mods', required=False, action='store_true', help = 'Displays Mods able to be downloaded by this program.')
#parser.add_argument('-i', required=False, action='store_true', help = 'Ignores the GTerminal Install Name for the DLL file and renames it to the Mod File Name.')
#parser.add_argument('-version', required=False, action='store_true', help = 'Lets you see the version of GTerminal you are using.')
#parser.add_argument('-keepvers', required=False, action='store_true', help = "Doesn't say when there is a new version anymore.")
#parser.add_argument('-discord', required=False, action='store_true', help = 'Opens the discord server.')
#parser.add_argument('-github', required=False, action='store_true', help = 'Opens the GitHub.')
command = input("Enter command here (without the dashes): ")

# trash, but shows if no arguments are made.
if command == '':
    print("Detected that you did not use any command. Start out by using --help.")

# shows version
elif command == 'version':
    print(version)

# if incorrect use of -i
elif command == 'i':
    print("Using -i is not supported on the EXE version, try upgrading to the python version!")

# awful way to install the mods
elif command == 'install':
    t = input("Which mod would you like to use?: ")
    if t == 'Blaku':
        install("https://cdn.discordapp.com/attachments/987981869813481512/1026938072807518268/Blaku_menu_v3_NotFinished.dll")
    elif t == 'Kman':
        install("https://cdn.discordapp.com/attachments/1016380735449477181/1025605291548618833/KmanMenu.dll")
    elif t == 'Guzzy':
        install("https://cdn.discordapp.com/attachments/1030261695714689025/1030261728254111824/Guzzy_Menu_X_V4.dll")
    elif t == 'GTK':
        install("https://cdn.discordapp.com/attachments/1016380735449477181/1029860716007653486/GorillaTaggingKid-Menu_6.5ForTests2.dll")
    elif t == 'Wihz':
        install("https://cdn.discordapp.com/attachments/1029854967382691840/1030244165390450758/WihzOrganizedMenu_v1.dll")
    elif t == 'Joker':
        install("https://cdn.discordapp.com/attachments/900938043442233345/1026286694107983882/J0ker_Menu_V1.4.dll")
    elif t == 'Moon':
        install("https://cdn.discordapp.com/attachments/1016380735449477181/1029795573194293299/moonso_1.dll")
    elif t == 'Zolo':
        install("https://cdn.discordapp.com/attachments/1029785882284269749/1030253586132770906/Zoloz_V9_.dll")
    elif t == 'Anna':
        install("https://cdn.discordapp.com/attachments/987186961150263346/994708566902591569/Annas_Mod_Menu_V2.dll")
    elif t == 'Pheonix':
        install("https://cdn.discordapp.com/attachments/985378173661368330/985378324601774180/XtraPheonixMenu.dll")
    elif t == 'Mirror':
        install("https://cdn.discordapp.com/attachments/1025619766179803136/1025629547464511528/BetterMirror.dll")
    else:
        print("Error 404. Retry and remember that GTerminal is cap sensitive. Still Need Help? Go to https://discord.gg/Fa36fvAdXE")

elif command == '':
    b = input("Are you sure you want to keep your version/disable it? (enable/disable/cancel): ")
    if b == 'enable':
        if os.path.exists("C:\\GTerminal\\keepvers.txt"):
            keep = "C:\\GTerminal\\keepvers.txt"
            with open(keep, 'w') as f:
                f.write("t")
            print("Success.")
        else:
            os.mkdir("C:\\GTerminal\\")
            keep = "C:\\GTerminal\\keepvers.txt"
            with open(keep, 'w') as f:
                f.write("t")
            print("Success.")
    elif b == 'disable':        
        if os.path.exists("C:\\GTerminal\\keepvers.txt"):
            keep = "C:\\GTerminal\\keepvers.txt"
            with open(keep, 'w') as f:
                f.write("f")
            print("Success.")
        else:
            os.mkdir("C:\\GTerminal\\")
            keep = "C:\\GTerminal\\keepvers.txt"
            with open(keep, 'w') as f:
                f.write("f")
            print("Success.")

# janky way to show mods
elif command == 'mods':
    os.system("start \"\" https://pastebin.com/raw/iDcsVwmA ")

# opens the discord
elif command == 'discord':
    os.system("start \"\" https://discord.gg/Fa36fvAdXE ")

#shows the version
elif command == 'version':
    print("Version: " + version)

#opens the github page
elif command == 'github':
    os.system("start \"\" https://github.com/Silentious/GTerminal ")

elif command == 'help':
    print('''Welcome, ''' + login + '''.
Please use a command to start.

<DISCLAIMER> Development Purposes Only.

options:
  --help        show this help message
  -install      Installs a mod.
  -mods         Displays Mods able to be downloaded by this program.
  -version      Lets you see the version of GTerminalEXE you are using.
  -keepvers     Doesn't say when there is a new version anymore.
  -discord      Opens the discord server.
  -github       Opens the GitHub.

Want your mod removed? Please email Silentious.Business@gmail.com. Messaging the owner in the discord will not be answered.
The menu will only be deleted if it is yours and there is a valid reason.''')
else:
    print('Command "'+ command + '" is not found!')