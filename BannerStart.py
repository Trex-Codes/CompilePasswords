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

header1Start = BannerColorRandom + """
  _____                      ___          _            
  /__   \_ __ _____  __      / __\___   __| | ___  ___  
    / /\/ '__/ _ \ \/ /____ / /  / _ \ / _` |/ _ \/ __| 
   / /  | | |  __/>  <_____/ /__| (_) | (_| |  __/\__ \ 
   \/   |_|  \___/_/\_\    \____/\___/ \__,_|\___||___/ 
""" + COLOR_BANNER_END
# Ogre

header2Start = BannerColorRandom +  """
  ████████╗██████╗ ███████╗██╗  ██╗      ██████╗ ██████╗ ██████╗ ███████╗███████╗
  ╚══██╔══╝██╔══██╗██╔════╝╚██╗██╔╝     ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝
     ██║   ██████╔╝█████╗   ╚███╔╝█████╗██║     ██║   ██║██║  ██║█████╗  ███████╗
     ██║   ██╔══██╗██╔══╝   ██╔██╗╚════╝██║     ██║   ██║██║  ██║██╔══╝  ╚════██║
     ██║   ██║  ██║███████╗██╔╝ ██╗     ╚██████╗╚██████╔╝██████╔╝███████╗███████║
     ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝      ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝
""" + COLOR_BANNER_END
#ANSI Shadow

header3Start = BannerColorRandom + """
      ▄▄▄▄▀ █▄▄▄▄ ▄███▄      ▄      ▄█▄    ████▄ ██▄   ▄███▄     ▄▄▄▄▄   
  ▀▀▀ █    █  ▄▀ █▀   ▀ ▀▄   █     █▀ ▀▄  █   █ █  █  █▀   ▀   █     ▀▄ 
      █    █▀▀▌  ██▄▄     █ ▀      █   ▀  █   █ █   █ ██▄▄   ▄  ▀▀▀▀▄   
     █     █  █  █▄   ▄▀ ▄ █       █▄  ▄▀ ▀████ █  █  █▄   ▄▀ ▀▄▄▄▄▀    
    ▀        █   ▀███▀  █   ▀▄     ▀███▀        ███▀  ▀███▀             
""" + COLOR_BANNER_END
# The Edge

header4Start = """
  \033[1;32m________                   \033[1;36m _________     _________             \033[0;m
  \033[1;32m___  __/_______________  __\033[1;36m __  ____/___________  /____________ \033[0;m
  \033[1;32m__  /  __  ___/  _ \_  |/_/\033[1;36m _  /    _  __ \  __  /_  _ \_  ___/ \033[0;m
  \033[1;32m_  /   _  /   /  __/_>  <  \033[1;36m / /___  / /_/ / /_/ / /  __/(__  )  \033[0;m
  \033[1;32m/_/    /_/    \___//_/|_|  \033[1;36m \____/  \____/\__,_/  \___//____/   \033[0;m
"""
# Speed

header5Start = BannerColorRandom + """
          _           _          _    _      _                _            _           _           _          _        
        /\ \        /\ \       /\ \/_/\    /\ \            /\ \          /\ \        /\ \        /\ \       / /\      
        \_\ \      /  \ \     /  \ \ \ \   \ \_\          /  \ \        /  \ \      /  \ \____  /  \ \     / /  \     
        /\__ \    / /\ \ \   / /\ \ \ \ \__/ / /         / /\ \ \      / /\ \ \    / /\ \_____\/ /\ \ \   / / /\ \__  
       / /_ \ \  / / /\ \_\ / / /\ \_\ \__ \/_/  ____   / / /\ \ \    / / /\ \ \  / / /\/___  / / /\ \_\ / / /\ \___\ 
      / / /\ \ \/ / /_/ / // /_/_ \/_/\/_/\__/\/\____/\/ / /  \ \_\  / / /  \ \_\/ / /   / / / /_/_ \/_/ \ \ \ \/___/ 
     / / /  \/_/ / /__\/ // /____/\    _/\/__\ \/____\/ / /    \/_/ / / /   / / / / /   / / / /____/\     \ \ \       
    / / /     / / /_____// /\____\/   / _/_/\ \ \    / / /         / / /   / / / / /   / / / /\____\/ _    \ \ \      
   / / /     / / /\ \ \ / / /______  / / /   \ \ \  / / /________ / / /___/ / /\ \ \__/ / / / /______/_/\__/ / /      
  /_/ /     / / /  \ \ / / /_______\/ / /    /_/ / / / /_________/ / /____\/ /  \ \___\/ / / /_______\ \/___/ /       
  \_\/      \/_/    \_\\/__________/\/_/     \_\/  \/____________\/_________/    \/_____/\/__________/\_____\/        
""" + COLOR_BANNER_END
# Impossible

header6Start = BannerColorRandom + """
  .-----..---. .----..-..-.     .----. .---. .----. .----. .----. 
  `-' '-'} }}_}} |__}\ {} / ___ | }`-'/ {-. \} {-. \} |__}{ {__-` 
    } {  | } \ } '__}/ {} \{___}| },-.\ '-} /} '-} /} '__}.-._} } 
    `-'  `-'-' `----'`-'`-'     `----' `---' `----' `----'`----'  
""" + COLOR_BANNER_END
# Braced

header7Start = BannerColorRandom + """
  _/_/_/_/_/                                              _/_/_/                  _/                    
     _/      _/  _/_/    _/_/    _/    _/              _/          _/_/      _/_/_/    _/_/      _/_/_/ 
    _/      _/_/      _/_/_/_/    _/_/    _/_/_/_/_/  _/        _/    _/  _/    _/  _/_/_/_/  _/_/      
   _/      _/        _/        _/    _/              _/        _/    _/  _/    _/  _/            _/_/   
  _/      _/          _/_/_/  _/    _/                _/_/_/    _/_/      _/_/_/    _/_/_/  _/_/_/      
""" + COLOR_BANNER_END
# Lean

def Random_HeaderStart():

  headers_START = [header1Start, header2Start, header3Start, header4Start, header5Start, header6Start]

  # Save in the variable choise of which banner will print
  BannerRandom = random.choice(headers_START)
  print(BannerRandom)

  # -- print Specific banner
  # print(header4Start)

  # -- print all banners
  # for i in headers_START:
    # print(i)

  # cont = 0 
  # while cont < len(headers_START):
    # print(headers_START[cont])
    # cont = cont + 1

# -- Print running this file
# Random_HeaderStart()