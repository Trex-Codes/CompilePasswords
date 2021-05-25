import os
import ctypes, sys
from subprocess import call

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


print("\033[0;36m", "  _____                      ___          _             ",  "\033[0;m")
print("\033[0;36m", " /__   \_ __ _____  __      / __\___   __| | ___  ___   ",  "\033[0;m")
print("\033[0;36m", "   / /\/ '__/ _ \ \/ /____ / /  / _ \ / _` |/ _ \/ __|  ",  "\033[0;m")
print("\033[0;36m ", " / /  | | |  __/>  <_____/ /__| (_) | (_| |  __/\__ \   ",  "\033[0;m")
print("\033[0;36m", "  \/   |_|  \___/_/\_\    \____/\___/ \__,_|\___||___/  ",  "\033[0;m")

print("\n","\033[1;31m[Info]","\033[0;m","\033[0;33mVerification of passwords ([TREX-CODES])\n")
print("\033[0;35m"," || wrotten in Python","\033[0;m")
print("\033[0;35m"," || If you can see this... sth is wrong")
print("\033[0;35m"," || All of my life be here >> https://github.com/Trex-Codes\n","\033[0;m")

def Person1():
	contador = 0
	while contador < 1:

		Data = {
			# Program, URL, User, Password
			# HERE WRITE THE PASSWORD LIKE A DICCIONARY 
			"Data01": "google ," "www.google.com ," "user123 ," "password123"
		}

		print("\n")
		for key in Data:
			print(key, end=" // ")

		print("\n")
		print("\033[1;34m")
		LogOption = input("  What you want to know: ")
		print("\033[0;m")

		if LogOption == "Data01":
			print(Data['Data01'])
		elif LogOption == "q" or LogOption == "q!" or LogOption == "quit":
			print("\n")
			print("\033[1;32m", "[+] SUCCESSFUL EXIT!!","\033[0;m")
			call('clear')
			contador = 2
		else: 
			print(" \033[4;31m","Data no exist yet","\033[4;m")

def Person2():
	contador = 0
	while contador < 1:

		Data = {
			# Program, URL, User, Password
			# HERE WRITE THE PASSWORD LIKE A DICCIONARY 
			"Data01": "google ," "www.google.com ," "user123 ," "password123"
		}

		print("\n")
		for key in Data:
			print(key, end=" // ")

		print("\n")

		print("\033[1;34m")
		LogOption = input("  What you want to know: ")
		print("\033[0;m")

		if LogOption == "Data01":
			print(Data['Data01'])
		elif LogOption == "q" or LogOption == "q!" or LogOption == "quit":
			print("\033[1;32m","  [+] SUCCESSFUL EXIT!!","\033[0;m")
			call('clear')
			contador = 2
		else: 
			print(" \033[4;31m","Data no exist yet","\033[4;m")

cont = 1
while cont != 0:

	print("\033[1;34m")
	optionPrinc = input("  ---------------------------------------------\n  [1] Check Password (Person1 - Person2)\n  [2] Generate filename.txt with all password\n  [q] Exit || Finish Program\n ----------------------------------------------  \n\n  [+] >> ")
	print("\n")
	print("\033[0;m")

	if optionPrinc == "1":
		coun2 = 0
		while coun2 == 0:

			call('clear')
			print("\033[1;35m")
			a = input('  ---------------------------------------------\n  [?] Who you are (P1-P2)\n  [q] Back\n  --------------------------------------------- \n\n  [+] >> ')
			call('clear')
			print("\033[0;m")

			if a == "p2": 
				call('clear')
				Person2()
				coun2 = 1
			elif a == "p1":
				Person1()
				coun2 = 1
			elif a == "q":
				print("\n")
				coun2 = 1

			else: 
				print("\n")
				print("\033[1;31m","  [+] Only (P1 or P2)","\033[0;m")

	elif optionPrinc == "2":
		print("# admin()")
	elif optionPrinc == "q":
		cont=cont-1
		# print("\033[1;32m"," [+] SUCCESSFUL EXIT!!","\033[0;m")
		print("\033[1;32m"," [+] SUCCESSFUL EXIT!!","\033[0;m\n\n")
		print("\033[1;32m","  ▄████▄  ▒█████  ███▄ ▄███▓█████     ▄▄▄▄   ▄▄▄      ▄████▄  ██ ▄█▀     ██████ ▒█████  ▒█████  ███▄    █     ▐██▌ ","\033[0;m")
		print("\033[1;32m"," ▒██▀ ▀█ ▒██▒  ██▓██▒▀█▀ ██▓█   ▀    ▓█████▄▒████▄   ▒██▀ ▀█  ██▄█▒    ▒██    ▒▒██▒  ██▒██▒  ██▒██ ▀█   █     ▐██▌ ","\033[0;m")
		print("\033[1;32m"," ▒▓█    ▄▒██░  ██▓██    ▓██▒███      ▒██▒ ▄█▒██  ▀█▄ ▒▓█    ▄▓███▄░    ░ ▓██▄  ▒██░  ██▒██░  ██▓██  ▀█ ██▒    ▐██▌ ","\033[0;m")
		print("\033[1;32m"," ▒▓▓▄ ▄██▒██   ██▒██    ▒██▒▓█  ▄    ▒██░█▀ ░██▄▄▄▄██▒▓▓▄ ▄██▓██ █▄      ▒   ██▒██   ██▒██   ██▓██▒  ▐▌██▒    ▓██▒ ","\033[0;m")
		print("\033[1;32m"," ▒ ▓███▀ ░ ████▓▒▒██▒   ░██░▒████▒   ░▓█  ▀█▓▓█   ▓██▒ ▓███▀ ▒██▒ █▄   ▒██████▒░ ████▓▒░ ████▓▒▒██░   ▓██░    ▒▄▄  ","\033[0;m")
		print("\033[1;32m"," ░ ░▒ ▒  ░ ▒░▒░▒░░ ▒░   ░  ░░ ▒░ ░   ░▒▓███▀▒▒▒   ▓▒█░ ░▒ ▒  ▒ ▒▒ ▓▒   ▒ ▒▓▒ ▒ ░ ▒░▒░▒░░ ▒░▒░▒░░ ▒░   ▒ ▒     ░▀▀▒ ","\033[0;m")
		print("\033[1;32m","   ░  ▒    ░ ▒ ▒░░  ░      ░░ ░  ░   ▒░▒   ░  ▒   ▒▒ ░ ░  ▒  ░ ░▒ ▒░   ░ ░▒  ░ ░ ░ ▒ ▒░  ░ ▒ ▒░░ ░░   ░ ▒░    ░  ░ ","\033[0;m")
		print("\033[1;32m"," ░       ░ ░ ░ ▒ ░      ░     ░       ░    ░  ░   ▒  ░       ░ ░░ ░    ░  ░  ░ ░ ░ ░ ▒ ░ ░ ░ ▒    ░   ░ ░        ░ ","\033[0;m")
		print("\033[1;32m"," ░ ░         ░ ░        ░     ░  ░    ░           ░  ░ ░     ░  ░            ░     ░ ░     ░ ░          ░     ░    ","\033[0;m")
		print("\033[1;32m"," ░                                         ░         ░                                                             ","\033[0;m")
		print("\033[1;32m"," 																												  ","\033[0;m")
		call('clear')
	else:
		call('clear')
		print("\033[1;31m","[!] Option Wrong!!  ||  Only ([1], [2] [q])\n","\033[0;m")