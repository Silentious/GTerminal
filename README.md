# GTerminal
The world's first terminal installer for mods on Gorilla Tag. 😎

(Disclaimer) Use only for development/educational purposes. I am not responsible for anything happening.
Most mods are checked for viruses, but it is not guaranteed. I highly think you should run your mod through DNSpy, and if anything suspicious is found, join the <a href="https://discord.gg/Fa36fvAdXE">Discord Server</a> and make a report.

*but there are so many other ways to install mods!!! why should I use GTerminal???*
- [x] Open Source
- [x] Free to use
- [x] Hub for many mods
- [x] Easy to install
- [x] Simple, 
- [x] It only takes a few seconds


## Installation
### 1. Unzip the file
This doesn't require explaining.

### 2. Install Python.
If you do not have python, please download it at https://www.python.org/downloads
If you want to download the buggy windows store version, open windows store and select a python version

### 3. Open file area in terminal
Command prompt works fine, but you can also use Windows Powershell.

### 4. Install Dependencies.
```console
# change directory to where you installed the files
$ py -m pip install -r requirements.txt
# or
$ pip install -r requirements.txt
```

## 2. Use
There are many ways to use this file. Usually, when using you'd want to do the following commands.
```console
# Before this, use CD and go to the file area. This can be done by right clicking in the file and doing "Open in Terminal"
$ py GTerminal.py
# or
$ python GTerminal.py
```

#### -install
Use -install to install the GT Mods. To see the mods, check out the -mods.
```console
# expected requirements:
$ py GTerminal.py -install <mod>
# or
$ python GTerminal.py -install <mod>
```
#### -uninstall
Uninstalls a mod of your choice by using an input
```console
# expected requirements:
$ py GTerminal.py -uninstall
# or
$ python GTerminal.py -uninstall
```
#### -mods
Opens the URL to check which mods GTerminal supports.
```console
$ py GTerminal.py -mods
# or
$ python GTerminal.py -mods
```
#### -i
Use -i with -install to name the downloaded file the install name that is used in the URL.

Example:
URL = https://cdn.discordapp.com/attachments/1000/1000/Cool_MODMENU!!!.dll
With -i:
**Cool_MODMENU!!!.dll**
Without -i:
**CoolMenu.dll**
```console
# expected requirements:
$ py GTerminal.py -install <mod> -i
# or
$ python GTerminal.py -install <mod> -i
```
#### -version
Shows which version of GTerminal you are using
```console
$ py GTerminal.py -version
# or
$ python GTerminal.py -version
```
#### -keepvers
When there is a new update, use this if you want to keep your version and don't want the update message to appear
```console
$ py GTerminal.py -keepvers
# or
$ python GTerminal.py -keepvers
```
#### -discord
Opens the <a href="https://discord.gg/Fa36fvAdXE">Discord server</a>
```console
$ py GTerminal.py -discord
# or
$ python GTerminal.py -discord
```
#### -github
Opens the <a href="https://github.com/Silentious/GTerminal">GitHub</a>
```console
$ py GTerminal.py -github
# or
$ python GTerminal.py -github
```

## MAYBE SOON:
- ~~Uninstall Feature~~
- ~~EXE Version~~
- Announcment Hide
- ???

## Versions

<div align="center">

**1.2.3**

</div>

- fix for _-config_ command

<div align="center">

**1.2.2**

</div>

- **JSON CONFIG**
- better text readability
- fixed double -version
- ??fixed mod sometimes not installing??=
- removed -keepvers and -i in favor of the config file
- no new mods

<div align="center">

**1.1.0**

</div>

- 5 New Menus
- Uninstall Feature
- Better text on new version message and mods
- Fixed mods sometimes not installing

<div align="center">

**1.0.0**

</div>

- Release
