from os import system
from colorama import Fore, Style, init
import sys


def firstmenu():
	system("bash ./src/firstmenu.sh")
	choice1 = int(input(f"{Fore.CYAN}{Style.BRIGHT}Enter The Number Here (1-5) : "))
	Style.RESET_ALL
	if choice1 == 1 :
		return choice1
	elif choice1 in [2,3]:
		st =  "\nSorry For inconvenience ! This Section is Pending\n"
		print(f"{Fore.RED}{Style.BRIGHT}{st}")
		Style.RESET_ALL
		sys.exit(1)
	elif choice1 == 4 :
		st =  "\nThanks For atleast starting it ;_; \n"
		print(f"{Fore.MAGENTA}{Style.BRIGHT}{st}")
		Style.RESET_ALL
	else:
		st =  "\nSorry ! You Entered an invalid choice...\n"
		print(f"{Fore.RED}{Style.BRIGHT}{st}")
		sys.exit(1)


def secondmenu():
	system("bash ./src/secondmenu.sh")
	choice2 = int(input(f"{Fore.CYAN}{Style.BRIGHT}Enter The Number of Players Here (1-3) : "))
	Style.RESET_ALL
	if choice2 == 1 :
		return choice2
	elif choice2 == 2 : 
		return choice2
	elif choice2 == 3 :
		st =  "\nThanks For atleast starting it ;_; \n"
		print(f"{Fore.MAGENTA}{Style.BRIGHT}{st}")
		Style.RESET_ALL
		sys.exit(1)
	else:
		st =  "\nSorry ! You Entered an invalid choice...\n"
		print(f"{Fore.RED}{Style.BRIGHT}{st}")
		sys.exit(1)

def thirdmenu():
	system("bash ./src/thirdmenu.sh")
	choice2 = int(input(f"{Fore.CYAN}{Style.BRIGHT}choose A WordList (1-3) : "))
	Style.RESET_ALL
	if choice2 == 1 :
		return choice2
	elif choice2 == 2 : 
		return choice2
	elif choice2 == 3 :
		st =  "\nThanks For atleast starting it ;_; \n"
		print(f"{Fore.MAGENTA}{Style.BRIGHT}{st}")
		Style.RESET_ALL
		sys.exit(1)
	else:
		st =  "\nSorry ! You Entered an invalid choice...\n"
		print(f"{Fore.RED}{Style.BRIGHT}{st}")
		sys.exit(1)