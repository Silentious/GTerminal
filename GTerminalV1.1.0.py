import argparse
import requests
import os
import urllib
import time
from halo import Halo
from os import link, startfile
from argparse import RawTextHelpFormatter
from urllib.request import urlopen

# way too many if commands
# no nutella children here pls 


# Welcome to the low effort GTerminal!


# pip install argparse, requests, urllib
# tracker
urllib.request.urlopen("https://pastebin.com/raw/wzZBav5Q")

# Shows the current version
version = "1.1.0"
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
            print("New Version found!: " + output + ". Your current version is " + version + ".")
            print("If you'd like to update, head to https://github.com/Silentious/GTerminal/\nIf you would like to not see this message again, do -keepvers") # update pls no keep version

announcment = urllib.request.urlopen('https://pastebin.com/raw/KgjGWbnX').read().decode('UTF-8')

if announcment != 'none': # makes announcment emergencies, don't delete.
    print(announcment)



# Use for welcome and install errors.
login = os.getlogin()

# Installs the mods
def install(mod):
    # Sets name to download name
    loading = Halo(text='Loading..', spinner='dots', color='blue')
    if args.i: # if name should be the real install name
        # DISCORD ATTACHMENTS SOMETIME NOW HAVE ANOTHER DIGIT BECAUSE OF ALL THE ATTACHMENTS BEING MADE >:(
        name = mod[78:] 
        br = name[:-4] 
        ft = br[0] 
        if ft in deadnumbers:
            newname = br[1:]
        else:
            newname = br
        print(newname)
    else:
    # Set name to actual name
        newname = args.install
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
        if os.path.exists("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Gorilla Tag\\BepInEx"):
            print("\nError 400. GTAG must be installed WITH Bepinex installled in the steam folder. Still need help? Go to https://discord.gg/Fa36fvAdXE")
            print("\nInstalling mods at desktop...")
            path = "C:\\Users\\" + login + "\\Desktop\\" + newname + ".dll"

    # actually installs the mods
    with open(path, 'wb') as f:
        try:
            f.write(requests.get(mod).content)
            print("\nFile created. Checking if data has transfered..")
        except OSError:
            loading.stop()
            print("\nError 507. Make sure you have enough storage. Still Need Help? Go to https://discord.gg/Fa36fvAdXE")
        except:
            print("\nUnknown Error. Need Help? Go to https://discord.gg/Fa36fvAdXE")
    time.sleep(2)
    success = os.path.getsize(path)
    #print(\nsuccess)
    time.sleep(1)
    if success == "0":
        print("\n", success)
        print("\nError 410. Mod did not receive any data, Please retry. Still Need Help? Go to https://discord.gg/Fa36fvAdXE")
    elif success == "1":
        print("\n", success)
        print("\nError 410. Mod did not receive any data, Please retry. Still Need Help? Go to https://discord.gg/Fa36fvAdXE")
    else:
        print("\nSuccessfully installed mod as " + newname + ".dll")
        loading.stop()

# create parser
parser = argparse.ArgumentParser(description="Welcome, " + login + ". \nPlease use a command to start.\n\n<DISCLAIMER> Development Purposes Only.", epilog="Want your mod removed? Please email Silentious.Business@gmail.com. Messaging the owner in the discord will not be answered.\nThe menu will only be deleted if it is yours and there is a valid reason.", formatter_class=RawTextHelpFormatter)

# adds arguments
parser.add_argument('-install', required=False, type=str, metavar='mod', help = 'Installs a mod.')
parser.add_argument('-uninstall', required=False, action='store_true', help = 'Uninstalls the Mods')
parser.add_argument('-mods', required=False, action='store_true', help = 'Displays Mods able to be downloaded by this program.')
parser.add_argument('-i', required=False, action='store_true', help = 'Ignores the GTerminal Install Name for the DLL file and renames it to the Mod File Name.')
parser.add_argument('-version', required=False, action='store_true', help = 'Lets you see the version of GTerminal you are using.')
parser.add_argument('-keepvers', required=False, action='store_true', help = "Doesn't say when there is a new version anymore.")
parser.add_argument('-discord', required=False, action='store_true', help = 'Opens the discord server.')
parser.add_argument('-github', required=False, action='store_true', help = 'Opens the GitHub.')

args = parser.parse_args()

# trash, but shows if no arguments are made.
if not args.install and not args.uninstall and not args.mods and not args.i and not args.version and not args.keepvers and not args.discord and not args.github:
    print("Detected that you did not use any command. Start out by using --help.")

# common sense
if args.install and args.uninstall:
    exit(code="You cannot install and uninstall at the same time!")

# shows version
if args.version:
    print(version)

# if incorrect use of -i
if args.i and not args.install:
        print("Please use -install with -i!")

# awful way to install the mods
if args.install:
    t = args.install
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
    elif t == 'Lean':
        install("https://cdn.discordapp.com/attachments/985380899984130098/994039458552881172/LeanMenu_FakeLag.dll")
    elif t == 'Sanity':
        install("https://cdn.discordapp.com/attachments/985593877941588008/991528641756401715/SanitysModV2.7.dll")
    elif t == 'Lele' or 'LeLe':
        install("https://cdn.discordapp.com/attachments/987134569742495744/987134592580460594/Leles_Menu_V4.dll")
    elif t == 'EyeClown':
        install("https://cdn.discordapp.com/attachments/985380209350033458/990034057775693875/EyeKlown_V1.0.dll")
    elif t == 'Flaymo':
        install("https://cdn.discordapp.com/attachments/985380738033668209/985380794690326548/Flaymo_Menu_V3.dll")
    else:
        print("Error 404. Retry and remember that GTerminal is cap sensitive. Still Need Help? Go to https://discord.gg/Fa36fvAdXE")



# uninstalls mods - V1.1.0
if args.uninstall:
    print("Printing Mods (If nothing shows then no mods are installed)...\n")
    for file in os.listdir("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Gorilla Tag\\BepInEx\\Plugins\\"):
        if file.endswith(".dll"):
            print(os.path.join(file))
            #unin = input("Which mod would you like to uninstall?: ")
    unin = input("Which mod would you like to uninstall?: ")
    ext = unin[:-4]
    if unin == 'quit':
        exit(code="Quit Successful.")
    try:
        os.remove("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Gorilla Tag\\BepInEx\\Plugins\\" + unin)
        print("Successfully removed " + unin + "!")
    except FileNotFoundError:
        print(unin + " was not found! Make sure to include the .dll at the end.\n")

#            try:
#                os.remove("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Gorilla Tag\\BepInEx\\Plugins\\" + unin)
#                print("Success!")
#            except:
#                print("Did not find a file named " + unin + ". Attempting to find a file with a ")
#                print("Error 503. Mod is not found.")
        #elif not file.endswith('.dll'):
        #    print("No mods found!")
        #    break

if args.keepvers:
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
if args.mods:
    os.system("start \"\" https://pastebin.com/raw/iDcsVwmA ")

# opens the discord
if args.discord:
    os.system("start \"\" https://discord.gg/Fa36fvAdXE ")

#shows the version
if args.version:
    print("Version: " + version)

#opens the github page
if args.github:
    os.system("start \"\" https://github.com/Silentious/GTerminal ")
