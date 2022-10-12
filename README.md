# GTerminal
Coolest way to install mods on Gorilla Tag. 😎

Windows Only.

(Disclaimer) Use only for development/educational purposes. I am not responsible for anything happening.
## Installation
### 1. Unzip the file
This doesn't require explaining.

### 2. Install Python.
If you do not install python, please download it at https://www.python.org/downloads

### 3. Install Dependencies.
```console
# change directory to where you installed the files
$ pip install -r requirements.txt
# some might get an error but Idk because i'm not gonna find out by deleting them.
```
### 4. Run in terminal
Command prompt works fine, but you can also use Windows Powershell.

## 2. Use
There are many ways to use this file. Usually, when using you'd want to do the following commands.
```console
# Before this, use CD and go to the file area.
$ python 
```

#### -install
Use -install to install the GT Mods. To see the mods, check out the -mods.
```console
# expected requirements:
$ python GTerminal.py -install <mod>
```
#### -mods
Opens the URL to check which mods GTerminal supports.
```console
$ python GTermina.py -mods
```
#### -i
Use -i with -install to name the downloaded file the install name that is used in the URL.
Example:
URL = https://cdn.discordapp.com/attachments/1000/000/Cool_MODMENU!!!.dll
With -i:
**Cool_MODMENU!!!.dll**
Without -i:
**CoolMenu.dll**
```console
# expected requirements:
$ python GTerminal.py -install <mods> -i
```
#### -version
Shows which version of GTerminal you are using
```console
$ python GTerminal.py -version
```
#### -keepvers
When there is a new update, use this if you want to keep your version and don't want the update message to appear
```console
$ python GTerminal.py -keepvers
```
#### -discord
Opens the <a href="https://discord.gg/Fa36fvAdXE">Discord server</a>
```console
$ python GTerminal.py -discord
```
#### -github
Opens the <a href="https://discord.gg/Fa36fvAdXE">GitHub</a>
```console
$ python GTerminal.py -github
```

## Versions


<div align="center">

**1.0.0**

</div>

- Release
