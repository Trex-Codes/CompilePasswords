import time
import os
import ctypes, sys 
from subprocess import call
import cowsay

from CompilePasswords import Init

def atbash_cypher(message):
        finalMessage = ""
        for letter in message.upper():
            if letter != " ":
                finalMessage += atbash[letter]
            else:
                finalMessage += " "

        finalMessage = finalMessage.lower().capitalize()

        return finalMessage

def Afirmative():
	os.system('clear')
	cowsay.ghostbusters("U right, letgoo!!!, u i'll pass")

def Negative():
	os.system('clear')
	cowsay.beavis("U sucks, get out of my fucking program! ")

call('clear')
q = input("Give me the key to open de door!: ")
os.system('clear')

atbash = {
			'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
        	'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
        	'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
        	'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
        	'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A', '.':'?', '?':'.'
        }

cowsay.dragon("Did u said: " +  q + "?")
input("Press enter to continue... ")


if atbash_cypher(q) == "Givcxlwvh":
	Afirmative()
	input("Press enter to continue... ")
	call('clear')
	Init()
elif atbash_cypher(q) != "Givcxlwvh":
	call('clear')
	Negative()
	call('clear')

"""
dict_keys(['beavis', 'cheese', 'daemon', 'cow',
'dragon', 'ghostbusters', 'kitty', 'meow', 'milk', 'pig',
'stegosaurus', 'stimpy', 'trex', 'turkey', 'turtle', 'tux'])
"""