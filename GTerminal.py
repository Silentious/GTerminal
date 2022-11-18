import argparse
import requests
import os
import urllib
import time
import json
from halo import Halo
from os import startfile
from argparse import RawTextHelpFormatter
from urllib.request import urlopen

# Welcome to the low effort GTerminal!

# no nutella children here pls 

# track
urllib.request.urlopen("https://pastebin.com/raw/wzZBav5Q")

try:
    with open('config.json', 'r') as config:
        data = json.load(config)
except FileNotFoundError:
    raise Exception ("Could not read config file. Make sure it exists and is in the same directory. Try downloading it from the github.")

#print(data)
ii = data['InstName-i']
keepvers = data['keepvers']
you = data['YourName']
double = data['DoubleCheck']


# Shows the current version
version = "1.2.3"

#makes a list of acceptable variable types
acceptableFT = [True, False]

# discord attachment numbers overflowed yay (Numbers to check for InstName-i config.)
deadnumbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '/']
# Obtains newest version
with urlopen('https://pastebin.com/raw/vRBSLqNe') as x:
    s = x.read()
output = s.decode("utf-8") #decode because computers suck

# Check for new version
if (version != output) and (keepvers == False):
    print("New Version found!: " + output + ". Your current version is " + version + ".")
    print("If you'd like to update, head to https://github.com/Silentious/GTerminal/\nIf you would like to not see this message again, do -keepvers") # update pls no keep version

announcment = urllib.request.urlopen('https://pastebin.com/raw/KgjGWbnX').read().decode('UTF-8')

if announcment != 'none': # makes announcment emergencies, don't delete.
    print(announcment)

if (ii or keepvers or you) not in acceptableFT:
    print(f"keep - {keepvers}\nyour - {you}")
    exit(code="Error with config files. Check if they are either true or false only.")

discord = 'https://discord.gg/Fa36fvAdXE'

# Use for welcome and install errors.
if you == True:
    login = os.getlogin()
elif you == False:
    login = 'User'

# Installs the mods
def install(mod):
    # Sets name to download name
    loading = Halo(text='Loading..', spinner='dots', color='blue')
    if ii == True: # if name should be the real install name
        # Discord attachments have different amount of characters so this kinda fixes that
        mod2 = mod[77:]
        mod2 = mod2[:-4] 
        ft = mod2[0] 
        for i in range(5):
            if ft in deadnumbers:
                newname = mod2[1:]
                ft = newname[0]
            else:
                newname = mod2
                break
    elif ii == False:
    # Set name to actual name
        newname = args.install
    if os.path.exists(f"C:\\Program Files (x86)\\Steam\\steamapps\\common\\Gorilla Tag\\BepInEx\\Plugins\\{newname}.dll"):
        print("Mod already installed. Overriding..")
    loading.start()
    try:
    # Check if BepInEx is installed
        path = f"C:\\Program Files (x86)\\Steam\\steamapps\\common\\Gorilla Tag\\BepInEx\\Plugins\\{newname}.dll"
    except:
    # If BepInEx isn't installed
        if os.path.exists("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Gorilla Tag"):
            loading.stop()
            print(f"\nError 400. GTAG must be installed in the steam folder. Still need help? Go to {discord}")
            print("\nInstalling mods at desktop...")
            path = f"C:\\Users\\{login}\\Desktop\\{newname}.dll"
        if os.path.exists("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Gorilla Tag\\BepInEx"):
            print(f"\nError 400. GTAG must be installed WITH Bepinex installled in the steam folder. Still need help? Go to {discord}")
            print("\nInstalling mods at desktop...")
            path = f"C:\\Users\\{login}\\Desktop\\{newname}.dll"

    # actually installs the mods
    with open(path, 'wb') as f:
        try:
            f.write(requests.get(mod).content)
            if double == True:
                print("\nFile created. Checking if data has transfered..")
            elif double == False:
                print('\nDid not check if data has transfered.')
        except OSError:
            loading.stop()
            print(f"\nError 507. Make sure you have enough storage. Still Need Help? Go to {discord}")
        #except:
        #    print(f"\nUnknown Error. Need Help? Go to {discord} . Also try deleting line 116 and line 117 in the code to see additional information.")
    time.sleep(2)
    success = os.path.getsize(path)
    #print(\nsuccess)
    time.sleep(1)
    if double == True:
        print(f"\nSuccessfully installed mod as {newname}.dll")
    elif double == False:
        if success == ("0" or "1"):
            print(f"\nData: {success}kb")
            print(f"\nError 410. Mod did not receive any data, Please retry. Still Need Help? Go to {discord}")
        else:
            print(f"\nSuccessfully installed mod as {newname}.dll")
        loading.stop()


# create parser
parser = argparse.ArgumentParser(description=f"Welcome, {login}. \nPlease use a command to start.\n\n<DISCLAIMER> Development Purposes Only.\n\nVersion: {version}", epilog="Want your mod removed? Please email Silentious.Business@gmail.com. Messaging the owner in the discord will not be answered.\nThe menu will only be deleted if it is yours and there is a valid reason.", formatter_class=RawTextHelpFormatter)

# adds arguments
parser.add_argument('-install', required=False, type=str, metavar='modname', help = 'Installs a mod.')
parser.add_argument('-uninstall', required=False, action='store_true', help = 'Uninstalls the Mods')
parser.add_argument('-mods', required=False, action='store_true', help = 'Displays Mods able to be downloaded by this program.')
parser.add_argument('-version', required=False, action='store_true', help = 'Lets you see the version of GTerminal you are using.')
parser.add_argument('-config', required=False, action='store_true', help = "Open the config file for editing")
parser.add_argument('-discord', required=False, action='store_true', help = 'Opens the discord server.')
parser.add_argument('-github', required=False, action='store_true', help = 'Opens the GitHub.')

args = parser.parse_args()

# trash, but shows if no arguments are made.
if not args.install and not args.uninstall and not args.mods and not args.version and not args.config and not args.discord and not args.github:
    print("Detected that you did not use any command. Start out by using --help.")

# common sense
if args.install and args.uninstall:
    exit(code="You cannot install and uninstall at the same time!")

# shows version
if args.version:
    print(f'Version: {version}')

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
    elif t == 'Lele':
        install("https://cdn.discordapp.com/attachments/987134569742495744/987134592580460594/Leles_Menu_V4.dll")
    elif t == 'EyeClown':
        install("https://cdn.discordapp.com/attachments/985380209350033458/990034057775693875/EyeKlown_V1.0.dll")
    elif t == 'Flaymo':
        install("https://cdn.discordapp.com/attachments/985380738033668209/985380794690326548/Flaymo_Menu_V3.dll")
    else:
        print(f"Error 404. Retry and remember that GTerminal is cap sensitive. Still Need Help? Go to {discord}")



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

# janky way to show mods
if args.mods:
    os.system("start \"\" https://pastebin.com/raw/iDcsVwmA ")

# opens the discord
if args.discord:
    os.system("start \"\" https://discord.gg/Fa36fvAdXE ")

# opens the config file
if args.config:
    os.startfile("config.json")
    print("Opened config file.")

#opens the github page
if args.github:
    os.system("start \"\" https://github.com/Silentious/GTerminal ")
