import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import random

# Colors 
COLOR_BANNER = '\033[0;36m'
COLOR_BANNER1 = '\033[1;36m'
COLOR_BANNER2 = '\033[1;31m'
COLOR_BANNER3 = '\033[1;32m'
COLOR_BANNER4 = '\033[0;33m'
COLOR_BANNER5 = '\033[1;33m'
COLOR_BANNER6 = '\033[0;35m'
COLOR_BANNER7 = '\033[1;35m'
COLOR_BANNER8 = '\033[1;34m'
COLOR_BANNER9 = '\033[1;30m'
COLOR_BANNER10 = '\033[1;37m'
COLOR_BANNER_END = '\033[0;m'

"""
BannerColorRandom = ''
BannerColorRandom = 0
- The code of Banner Colors will be in the top of the def() because,
 the variable staying in the def, show ERROR '' dont be defin before'
 and the variable dont allow to concatenate str + int.

- Other Bugs is in to console, to print the value of  var (BannerColorRandom = 0),
   print the zero and this dont allow print the Banners ASCII
   
- It Dont declare the var in String (global), this generate error,
   and in the moment to add repr() to convert to string, run all showing 
   the code ANSI in str. 

- Where the process of change colors doesnt work, and the styles color
 for default will be white
"""

headers_END_COLOR = [COLOR_BANNER, COLOR_BANNER1, COLOR_BANNER2, COLOR_BANNER3, COLOR_BANNER4, COLOR_BANNER5, COLOR_BANNER6, COLOR_BANNER7, COLOR_BANNER8, COLOR_BANNER9, COLOR_BANNER10]
BannerColorRandom = random.choice(headers_END_COLOR)

header1End = BannerColorRandom + """
  ▒██▀ ▀█ ▒██▒  ██▓██▒▀█▀ ██▓█   ▀    ▓█████▄▒████▄   ▒██▀ ▀█  ██▄█▒    ▒██    ▒▒██▒  ██▒██▒  ██▒██ ▀█   █     ▐██▌ 
   ▄████▄  ▒█████  ███▄ ▄███▓█████     ▄▄▄▄   ▄▄▄      ▄████▄  ██ ▄█▀     ██████ ▒█████  ▒█████  ███▄    █     ▐██▌ 
  ▒▓█    ▄▒██░  ██▓██    ▓██▒███      ▒██▒ ▄█▒██  ▀█▄ ▒▓█    ▄▓███▄░    ░ ▓██▄  ▒██░  ██▒██░  ██▓██  ▀█ ██▒    ▐██▌ 
  ▒▓▓▄ ▄██▒██   ██▒██    ▒██▒▓█  ▄    ▒██░█▀ ░██▄▄▄▄██▒▓▓▄ ▄██▓██ █▄      ▒   ██▒██   ██▒██   ██▓██▒  ▐▌██▒    ▓██▒ 
  ▒ ▓███▀ ░ ████▓▒▒██▒   ░██░▒████▒   ░▓█  ▀█▓▓█   ▓██▒ ▓███▀ ▒██▒ █▄   ▒██████▒░ ████▓▒░ ████▓▒▒██░   ▓██░    ▒▄▄  
  ░ ░▒ ▒  ░ ▒░▒░▒░░ ▒░   ░  ░░ ▒░ ░   ░▒▓███▀▒▒▒   ▓▒█░ ░▒ ▒  ▒ ▒▒ ▓▒   ▒ ▒▓▒ ▒ ░ ▒░▒░▒░░ ▒░▒░▒░░ ▒░   ▒ ▒     ░▀▀▒ 
    ░  ▒    ░ ▒ ▒░░  ░      ░░ ░  ░   ▒░▒   ░  ▒   ▒▒ ░ ░  ▒  ░ ░▒ ▒░   ░ ░▒  ░ ░ ░ ▒ ▒░  ░ ▒ ▒░░ ░░   ░ ▒░    ░  ░ 
  ░       ░ ░ ░ ▒ ░      ░     ░       ░    ░  ░   ▒  ░       ░ ░░ ░    ░  ░  ░ ░ ░ ░ ▒ ░ ░ ░ ▒    ░   ░ ░        ░ 
  ░ ░         ░ ░        ░     ░  ░    ░           ░  ░ ░     ░  ░            ░     ░ ░     ░ ░          ░     ░    
  ░                                         ░         ░                                                             
""" + COLOR_BANNER_END
# bloody

header2End = BannerColorRandom + """
     ______                        ____             __      _____                      __
    / ________  ____ ___  ___     / __ )____ ______/ /__   / ___/____  ____  ____     / /
   / /   / __ \/ __ `__ \/ _ \   / __  / __ `/ ___/ //_/   \__ \/ __ \/ __ \/ __ \   / / 
  / /___/ /_/ / / / / / /  __/  / /_/ / /_/ / /__/ ,<     ___/ / /_/ / /_/ / / / /  /_/  
  \____/\____/_/ /_/ /_/\___/  /_____/\__,_/\___/_/|_|   /____/\____/\____/_/ /_/  (_)   
""" + COLOR_BANNER_END
#Slant

header3End = BannerColorRandom + '''
     ___                                 ___                  _              ___                                  _    
    / __|   ___   _ __    ___     o O O | _ )  __ _    __    | |__    o O O / __|   ___    ___   _ _      o O O  | |   
   | (__   / _ \ | '  \  / -_)   o      | _ \ / _` |  / _|   | / /   o      \__ \  / _ \  / _ \ | ' \    o       |_|   
    \___|  \___/ |_|_|_| \___|  TS__[O] |___/ \__,_|  \__|_  |_\_\  TS__[O] |___/  \___/  \___/ |_||_|  TS__[O] _(_)_  
  _|"""""_|"""""_|"""""_|"""""|{======_|"""""_|"""""_|"""""_|"""""|{======_|"""""_|"""""_|"""""_|"""""|{======_| """ | 
  "`-0-0-"`-0-0-"`-0-0-"`-0-0-./o--000"`-0-0-"`-0-0-"`-0-0-"`-0-0-./o--000"`-0-0-"`-0-0-"`-0-0-"`-0-0-./o--000"`-0-0-' 
''' + COLOR_BANNER_END
#Train

header4End = BannerColorRandom + """
   ▄▄·     • ▌ ▄ ·.▄▄▄ .    ▄▄▄▄· ▄▄▄· ▄▄·▄ •▄     .▄▄ ·           ▐ ▄     ▄▄ 
  ▐█ ▌▪    ·██ ▐███▀▄.▀·    ▐█ ▀█▐█ ▀█▐█ ▌█▌▄▌▪    ▐█ ▀.▪    ▪    •█▌▐█    ██▌
  ██ ▄▄▄█▀▄▐█ ▌▐▌▐█▐▀▀▪▄    ▐█▀▀█▄█▀▀███ ▄▐▀▀▄·    ▄▀▀▀█▄▄█▀▄ ▄█▀▄▐█▐▐▌    ▐█·
  ▐███▐█▌.▐██ ██▌▐█▐█▄▄▌    ██▄▪▐▐█ ▪▐▐███▐█.█▌    ▐█▄▪▐▐█▌.▐▐█▌.▐██▐█▌    .▀ 
  ·▀▀▀ ▀█▄▀▀▀  █▪▀▀▀▀▀▀     ·▀▀▀▀ ▀  ▀·▀▀▀·▀  ▀     ▀▀▀▀ ▀█▄▀▪▀█▄▀▀▀ █▪     ▀ 
""" + COLOR_BANNER_END
#Elite

header5End = BannerColorRandom + """
   _                  _               __                 
  /   _  ._ _   _    |_)  _.  _ |    (_   _   _  ._    | 
  \_ (_) | | | (/_   |_) (_| (_ |<   __) (_) (_) | |   o                                                  
""" + COLOR_BANNER_END
# Mini

header6End = BannerColorRandom + """
   ____ ____ ____ ____ _________ ____ ____ ____ ____ _________ ____ ____ ____ ____ _________ ____ 
  ||C |||o |||m |||e |||       |||B |||a |||c |||k |||       |||S |||o |||o |||n |||       |||! ||
  ||__|||__|||__|||__|||_______|||__|||__|||__|||__|||_______|||__|||__|||__|||__|||_______|||__||
  |/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/_______\|/__\|
""" + COLOR_BANNER_END
# Smaill Keyboard

def Random_HeaderEnd():
  headers_END = [header1End, header2End, header3End, header4End, header5End, header6End]

  # save in the variable choise of which banner will print
  BannerRandom = random.choice(headers_END)
  # print(BannerRandom)

  # print(specific banner)
  # print(header1End)

  # -- print all banners 
  # for i in headers_END:
    # print(i)

  # cont = 0
  # while cont < len(headers_END):
    # print(headers_END[cont])
    # cont = cont + 1

# -- print running this file
Random_HeaderEnd()