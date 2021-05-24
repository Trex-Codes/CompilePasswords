import os
import ctypes, sys
from subprocess import call


print("\033[0;36m", "  _____                      ___          _             ",  "\033[0;m")
print("\033[0;36m", " /__   \_ __ _____  __      / __\___   __| | ___  ___   ",  "\033[0;m")
print("\033[0;36m", "   / /\/ '__/ _ \ \/ /____ / /  / _ \ / _` |/ _ \/ __|  ",  "\033[0;m")
print("\033[0;36m ", " / /  | | |  __/>  <_____/ /__| (_) | (_| |  __/\__ \   ",  "\033[0;m")
print("\033[0;36m", "  \/   |_|  \___/_/\_\    \____/\___/ \__,_|\___||___/  ",  "\033[0;m")

print("\n","\033[1;31m","[Info]","\033[0;m","\033[0;33m","Verification of passwords (ONLY FAMILY [MOM-TREX])\n")
print("\033[0;35m"," || wrotten in Python","\033[0;m")
print("\033[0;35m"," || If you can see this... sth is wrong")
print("\033[0;35m"," || All of my life be here >> https://github.com/Trex-Codes\n","\033[0;m")

def Aida():

	contador = 0
	while contador < 1:

		print("\033[1;34m")
		LogOption = input("  What you want to know: ")
		print("\033[0;m")

		if LogOption == "q" or LogOption == "q!" or LogOption == "quit":
			print("\n")
			print("\033[1;32m", "[+] SUCCESSFUL EXIT!!","\033[0;m")
			call('clear')
			contador = 2
		else: 
			print(" \033[4;31m","Data no exist yet","\033[4;m")

def Trex():

	contador = 0
	while contador < 1:

		print("\033[1;34m")
		LogOption = input("  What you want to know: ")
		print("\033[0;m")

		if LogOption == "q" or LogOption == "q!" or LogOption == "quit":
			print("\033[1;32m","  [+] SUCCESSFUL EXIT!!","\033[0;m")
			call('clear')
			contador = 2
		else: 
			print(" \033[4;31m","Data no exist yet","\033[4;m")


cont = 1
while cont != 0:

	print("\033[1;34m")
	optionPrinc = input("  ---------------------------------------------\n  [1] Check Password (TREX - AIDA)\n  [2] Generate filename.txt with all password\n  [q] Exit || Finish Program\n ----------------------------------------------  \n\n  [+] >> ")
	print("\n")
	print("\033[0;m")

	if optionPrinc == "1":

		coun2 = 0
		while coun2 == 0:

			call('clear')
			print("\033[1;35m")
			a = input('  ---------------------------------------------\n  [?] Who you are (A-T)\n  [q] Back\n  --------------------------------------------- \n\n  [+] >> ')
			call('clear')
			print("\033[0;m")

			if a == "A" or a == "a": 
				call('clear')
				Aida()
				coun2 = 1
			elif a == "T" or a == "t":
				Trex()
				coun2 = 1
			elif a == "q":
				print("\n")
				coun2 = 1

			else: 
				print("\n")
				print("\033[1;31m","  [+] Only (A or T)","\033[0;m")

	elif optionPrinc == "2":
		print("# admin()")

	elif optionPrinc == "q":
		cont=cont-1
		print("\033[1;32m"," [+] SUCCESSFUL EXIT!!","\033[0;m")

	else:
		call('clear')
		print("\033[1;31m","[!] Option Wrong!!  ||  Only ([1], [2] [q])\n","\033[0;m")



