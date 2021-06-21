
import os 
import ctypes, sys 
from subprocess import call

<<<<<<< HEAD
=======
# import file Banners (START-END)
from BannerStart import Random_HeaderStart
from BannerEnd import Random_HeaderEnd

import sys
>>>>>>> Update_Banners
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

<<<<<<< HEAD
# Colors 
COLOR_BANNER = '\033[0;36m'
ERROR = '\033[1;31m'
ERROR_DATA = '\033[4;31m'
SUCCESS = '\033[1;32m'
MESSAGE = '\033[0;33m'
MESSAGE2 = '\033[0;35m'
MESSAGE3 = '\033[1;35m'
MESSAGE4 = '\033[1;34m'
END = '\033[0;m'

Banner = COLOR_BANNER + '''
___________                               _________            .___             
\__    ___/______   ____ ___  ___         \_   ___ \  ____   __| _/____   ______
  |    |  \_  __ \_/ __ \\  \/  /  ______ /    \  \/ /  _ \ / __ |/ __ \ /  ___/
  |    |   |  | \/\  ___/ >    <  /_____/ \     \___(  <_> ) /_/ \  ___/ \___ \ 
  |____|   |__|    \___  >__/\_ \          \______  /\____/\____ |\___  >____  >
                       \/      \/                 \/            \/    \/     \/  '''

print(Banner)                       
print("\n",ERROR,"[Info]",MESSAGE,"Verification of passwords ([2 PERSONS OR MORE..])\n")
print(MESSAGE2," || Wrotten in Python")
print(MESSAGE2," || coded by Trex-Codes")
print(MESSAGE2," || >> https://github.com/Trex-Codesn", END)
=======
# funcion of headers
Random_HeaderStart()

print("\n","\033[1;31m[Info]","\033[0;m","\033[0;33mVerification of passwords ([TREX-CODES])\n")
print("\033[0;35m"," || wrotten in Python","\033[0;m")
print("\033[0;35m"," || Coded by Trex-Codes")
print("\033[0;35m"," || >> https://github.com/Trex-Codes\n","\033[0;m")
>>>>>>> Update_Banners

def Person1():
	contador = 0
	while contador < 1:

		Data = {
			# Program-App, Url, user, password
			"Gmail": "https://mail.google.com/mail/u/0/ ," "tfsf123@gmail.com ," "Hola123",
		}

		print('\n')
		for key in Data:
			print(key, end=" || ")

		print('\n')
		print(MESSAGE4)
		logOption = input("  What you want to know: ")
		print(END)

		if logOption == "Gmail" or logOption == "gmail" or logOption == "correo":
			print(Data['Gmail'])
		elif logOption == "q" or logOption == "!q" or logOption == "quit":
			print('\n')
			print(SUCCESS,"[+] SUCCESSFUL EXIT!!",END)
			call('clear')
			contador = 2
		else:
			print(ERROR_DATA,"Data no exist yet",END)

def Person2():
	contador = 0
	while contador < 1:

		Data = {
			# Program, Url, user, password
			"Gmail": "https://mail.google.com/mail/u/0/ ," "tfsf123@gmail.com ," "Hola123",

		}

		print('\n')
		for key in Data:
			print(key, end=" || ")

		print('\n')
		print(MESSAGE4)
		logOption = input("  What you want to know: ")
		print(END)

		if logOption == "Gmail" or LogOption == "gmail" or LogOption == "correo":
			print(Data['Gmail'])
		elif logOption == "q" or LogOption == "!q" or LogOption == "quit":
			print('\n')
			print(SUCCESS,"[+] SUCCESSFUL EXIT!!",END)
			call('clear')
			contador = 2
		else:
			print(ERROR_DATA,"Data no exist yet",END)

cont = 1
while cont != 0:
	print(MESSAGE4)
	optionPrinc = input(" ---------------------------------------------\n  [1] Check Password (Person1 - Person2)\n  [q] Exit || Finish Program\n ---------------------------------------------\n\n [+] >> ")
	print('\n')
	print(END)

	if optionPrinc == "1":
		coun2 = 0
		while coun2 == 0:
			call('clear')
			print(MESSAGE3)
			SelectPerson = input(' ---------------------------------------------\n  [?] Who you are (P1-P2)\n  [q] Back\n ---------------------------------------------\n\n [+] >> ')
			call('clear')			
			print(END)

			if SelectPerson == "p1":
				call('clear')
				Person1()
				coun2 = 1
			elif SelectPerson == "q":
				print('\n')
				coun2 = 1
			else:
				print('\n')
				print(ERROR,"[!] Only (P1 or P2)", END)
	elif optionPrinc == "q":
<<<<<<< HEAD
		cont = cont -1
		print(SUCCESS,"[+] SUCCESSFUL EXIT!!",END,"\n")
		Banner_End = SUCCESS + '''
   ▄████▄   ▒█████   ███▄ ▄███▓▓█████     ▄▄▄▄    ▄▄▄       ▄████▄   ██ ▄█▀     ██████  ▒█████   ▒█████   ███▄    █     ▐██▌ 
  ▒██▀ ▀█  ▒██▒  ██▒▓██▒▀█▀ ██▒▓█   ▀    ▓█████▄ ▒████▄    ▒██▀ ▀█   ██▄█▒    ▒██    ▒ ▒██▒  ██▒▒██▒  ██▒ ██ ▀█   █     ▐██▌ 
  ▒▓█    ▄ ▒██░  ██▒▓██    ▓██░▒███      ▒██▒ ▄██▒██  ▀█▄  ▒▓█    ▄ ▓███▄░    ░ ▓██▄   ▒██░  ██▒▒██░  ██▒▓██  ▀█ ██▒    ▐██▌ 
  ▒▓▓▄ ▄██▒▒██   ██░▒██    ▒██ ▒▓█  ▄    ▒██░█▀  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄      ▒   ██▒▒██   ██░▒██   ██░▓██▒  ▐▌██▒    ▓██▒ 
  ▒ ▓███▀ ░░ ████▓▒░▒██▒   ░██▒░▒████▒   ░▓█  ▀█▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄   ▒██████▒▒░ ████▓▒░░ ████▓▒░▒██░   ▓██░    ▒▄▄  
  ░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ░  ░░░ ▒░ ░   ░▒▓███▀▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒   ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒     ░▀▀▒ 
    ░  ▒     ░ ▒ ▒░ ░  ░      ░ ░ ░  ░   ▒░▒   ░   ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░   ░ ░▒  ░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░░   ░ ▒░    ░  ░ 
  ░        ░ ░ ░ ▒  ░      ░      ░       ░    ░   ░   ▒   ░        ░ ░░ ░    ░  ░  ░  ░ ░ ░ ▒  ░ ░ ░ ▒     ░   ░ ░        ░ 
  ░ ░          ░ ░         ░      ░  ░    ░            ░  ░░ ░      ░  ░            ░      ░ ░      ░ ░           ░     ░    
  ░                                            ░           ░                                                                 
  		'''
		print(Banner_End)
=======
		cont=cont-1
		print("\033[1;32m"," [+] SUCCESSFUL EXIT!!","\033[0;m")
		Random_HeaderEnd()
>>>>>>> Update_Banners
		call('clear')
	else:
		call('clear')
		print(ERROR,"[!] Option Wrong!! || Only ([1], [2], [q]\n",END)

