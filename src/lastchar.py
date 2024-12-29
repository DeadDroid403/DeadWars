from os import system
from src import decorations
import colorama as cl
import random
import threading
import select
import sys
import time

cl.init()
# {cl.Fore.GREEN}{cl.Style.BRIGHT} {cl.Style.RESET_ALL}

def Last_char(num):
    # variables intializations
    nameofwl = givewordlist(num)
    Wordlist = []
    player1 = ""
    player2 = ""
    pl1health = 5
    pl2health = 5
    timeout = 30

    # Starting setup
    with open(nameofwl, 'r') as fp:
        for line in fp.readlines():
            Wordlist.append(line.strip())
    system('clear')
    decorations.logo()
    decorations.rocket()

    # Printing the Rules
    print(f"{cl.Fore.GREEN}{cl.Style.BRIGHT}\nStarting The Last Char GaMe...\n{cl.Style.RESET_ALL}")
    print(f"{cl.Fore.RED}{cl.Style.BRIGHT} (o_o) Game Rules{cl.Style.RESET_ALL}")
    print(f"{cl.Fore.BLUE}{cl.Style.BRIGHT}1. You will be given a Word to start With...")
    print(f"{cl.Fore.BLUE}{cl.Style.BRIGHT}2. Players, will provide another word related to the category...")
    print(f"{cl.Fore.BLUE}{cl.Style.BRIGHT}3. Each provided word must start with the Last Character of the previous word...")
    print(f"{cl.Fore.BLUE}{cl.Style.BRIGHT}4. Words can't be repeated or unrelated to the Map...")
    print(f"{cl.Fore.BLUE}{cl.Style.BRIGHT}5. Type \'byedead\' anytime to exit from the game...\n\n{cl.Style.RESET_ALL}")
    player1 = input(f"{cl.Fore.CYAN}{cl.Style.BRIGHT}Enter Player 1 Name:- ")
    player2 = input("Enter Player 2 Name:- ")
    cl.Style.RESET_ALL

    # Main Game Logic
    oldword = random.choice(Wordlist)
    Wordlist.remove(oldword)
    print(f"\n{cl.Fore.YELLOW}{cl.Style.BRIGHT}Your starting Word is : {oldword}")
    while True:
        prm = f"{cl.Fore.CYAN}{cl.Style.BRIGHT}{player1} [Health = {pl1health}]: Enter word starting with \'{oldword[-1]}\' :- {cl.Fore.YELLOW}{cl.Style.BRIGHT}"
        p1word = user_input_timer(prm , timeout)
        if p1word == 'byedead':
            st =  "\nThanks For Playing... See U Soon ^._.^ \n"
            print(f"{cl.Fore.MAGENTA}{cl.Style.BRIGHT}{st}")
            cl.Style.RESET_ALL
            sys.exit(1)
        if p1word not in Wordlist:
            pl1health -= 1
            if p1word == "tttt":
                print(f"\n{cl.Fore.RED}{cl.Style.BRIGHT}Timeout : {player1} ! has health left {pl1health}")
            else:
                print(f"{cl.Fore.RED}{cl.Style.BRIGHT}Wrong guess : {player1} ! has health left {pl1health}")
            if pl1health ==  0:
                decorations.rocket()
                print(f"{cl.Fore.GREEN}{cl.Style.BRIGHT}\n -o- Hurray {player2} is the Winner of the GAME...\n{cl.Style.RESET_ALL}")
                print(f"{cl.Fore.GREEN}{cl.Style.BRIGHT} -o- Thanks for Playing...{cl.Style.RESET_ALL}")
                decorations.rocket()
                sys.exit(1)
            
            oldword = random.choice(Wordlist)
            Wordlist.remove(oldword)
            print(f"\n{cl.Fore.YELLOW}{cl.Style.BRIGHT}Your New Word is : {oldword}")
        else:
            oldword = p1word
            Wordlist.remove(oldword)
            print()

        prm = f"{cl.Fore.CYAN}{cl.Style.BRIGHT}{player2} [Health = {pl2health}]: Enter word starting with \'{oldword[-1]}\' :- {cl.Fore.YELLOW}{cl.Style.BRIGHT}"
        p2word = user_input_timer(prm , timeout)
        if p2word == 'byedead':
            st =  "\nThanks For Playing... See U Soon ^._.^ \n"
            print(f"{cl.Fore.MAGENTA}{cl.Style.BRIGHT}{st}")
            cl.Style.RESET_ALL
            sys.exit(1)
        if p2word not in Wordlist:
            pl2health -= 1
            if p1word == "tttt":
                print(f"\n{cl.Fore.RED}{cl.Style.BRIGHT}Timeout : {player2} ! has health left {pl2health}")
            else:
                print(f"{cl.Fore.RED}{cl.Style.BRIGHT}Wrong guess : {player2} ! has health left {pl2health}")
            if pl2health ==  0:
                decorations.rocket()
                print(f"{cl.Fore.GREEN}{cl.Style.BRIGHT}\n -o- Hurray {player1} is the Winner of the GAME...\n{cl.Style.RESET_ALL}")
                print(f"{cl.Fore.GREEN}{cl.Style.BRIGHT} -o- Thanks for Playing...{cl.Style.RESET_ALL}")
                decorations.rocket()
                sys.exit(1)
            oldword = random.choice(Wordlist)
            Wordlist.remove(oldword)
            print(f"\n{cl.Fore.YELLOW}{cl.Style.BRIGHT}Your New Word is : {oldword}")
        else:
            oldword = p2word
            Wordlist.remove(oldword)
            print()

def last_char_single(num):
    # variables intializations
    nameofwl = givewordlist(num)
    Wordlist = []
    player = ""
    plhealth = 5
    timeout = 30
    score = 0
    oldscore = 0

    # Starting setup
    with open(nameofwl, 'r') as fp:
        for line in fp.readlines():
            Wordlist.append(line.strip())
    system('clear')
    decorations.logo()
    decorations.rocket()

    # Printing the Rules
    print(f"{cl.Fore.GREEN}{cl.Style.BRIGHT}\nStarting The Last Char GaMe...\n{cl.Style.RESET_ALL}")
    print(f"{cl.Fore.RED}{cl.Style.BRIGHT} (o_o) Game Rules{cl.Style.RESET_ALL}")
    print(f"{cl.Fore.BLUE}{cl.Style.BRIGHT}1. You will be given a Word to start With...")
    print(f"{cl.Fore.BLUE}{cl.Style.BRIGHT}2. Players, will provide another word related to the category...")
    print(f"{cl.Fore.BLUE}{cl.Style.BRIGHT}3. Each provided word must start with the Last Character of the previous word...")
    print(f"{cl.Fore.BLUE}{cl.Style.BRIGHT}4. Words can't be repeated or unrelated to the Map...")
    print(f"{cl.Fore.BLUE}{cl.Style.BRIGHT}5. Type \'byedead\' anytime to exit from the game...\n\n{cl.Style.RESET_ALL}")
    player = input(f"{cl.Fore.CYAN}{cl.Style.BRIGHT}Enter Your Name:- ")
    oldscore = int(input(f"{cl.Fore.CYAN}{cl.Style.BRIGHT}Enter your previous score (if not, Enter 0) :- "))
    cl.Style.RESET_ALL

    # Main Game Logic
    oldword = random.choice(Wordlist)
    Wordlist.remove(oldword)
    print(f"\n{cl.Fore.YELLOW}{cl.Style.BRIGHT}Your starting Word is : {oldword}")
    while True:
        prm = f"{cl.Fore.CYAN}{cl.Style.BRIGHT}{player} [Health = {plhealth},Score = {score}]: Enter word starting with \'{oldword[-1]}\' :- {cl.Fore.YELLOW}{cl.Style.BRIGHT}"
        p1word = user_input_timer(prm , timeout)
        if p1word == 'byedead':
            print(f"{cl.Fore.GREEN}{cl.Style.BRIGHT}\n -o- Are you going, {player}!\n No Worries ! Your Score is {score} \n{cl.Style.RESET_ALL}")
            st =  "\nThanks For Playing... See U Soon ^._.^ \n"
            print(f"{cl.Fore.MAGENTA}{cl.Style.BRIGHT}{st}")
            cl.Style.RESET_ALL
            sys.exit(1)
        if p1word not in Wordlist:
            plhealth -= 1
            if p1word == "tttt":
                print(f"\n{cl.Fore.RED}{cl.Style.BRIGHT}Timeout : {player} ! has health left {plhealth}")
            else:
                print(f"{cl.Fore.RED}{cl.Style.BRIGHT}Wrong guess : {player} ! has health left {plhealth}")
            if plhealth ==  0:
                decorations.rocket()
                print(f"{cl.Fore.GREEN}{cl.Style.BRIGHT}\n -o- BTW You can't remember Everything, {player}!{cl.Style.RESET_ALL}")
                if score > oldscore:
                    print(f"{cl.Fore.GREEN}{cl.Style.BRIGHT}\n -o- But Yeah ! You made it up !\n -o- Your New score is - {score} {cl.Style.RESET_ALL}")
                else:
                    print(f"{cl.Fore.GREEN}{cl.Style.BRIGHT}\n -o- You scored Lower than before !\n -o- Your scores are -> [previous score = {oldscore} , New score = {score}]\n{cl.Style.RESET_ALL}")
                print(f"{cl.Fore.GREEN}{cl.Style.BRIGHT} -o- Thanks for Playing...{cl.Style.RESET_ALL}")
                decorations.rocket()
                sys.exit(1)
            
            oldword = random.choice(Wordlist)
            Wordlist.remove(oldword)
            print(f"\n{cl.Fore.YELLOW}{cl.Style.BRIGHT}Your New Word is : {oldword}")
        else:
            oldword = p1word
            score += 1
            Wordlist.remove(oldword)
            print()

def update_timer(stop_flag, timeout):
    for remaining in range(timeout, -1, -1):
        if stop_flag[0]:
            break
        # Save cursor position, move to top, print timer, restore cursor position
        sys.stdout.write("\033[s")
        sys.stdout.write("\033[H")
        sys.stdout.write(f"Timer: {remaining}                                                                                                      \n")
        sys.stdout.write("-" * 100)
        sys.stdout.write("\033[u")
        sys.stdout.flush()
        time.sleep(1)
    # Clear the timer when done = Save, move, clear, and restore
    sys.stdout.write("\033[s\033[H\033[K\033[u")

def user_input_timer(prompt, timeout):
    user_input = None  
    stop_flag = [False] 

    def get_input():
        nonlocal user_input
        print(prompt, end="", flush=True)
        ready, _, _ = select.select([sys.stdin], [], [], timeout)
        if ready: 
            user_input = sys.stdin.readline().strip()
        else:
            user_input = "tttt"  # Simulate fake input after timeout
        stop_flag[0] = True  # Stop the timer

    # Start timer thread
    timer_thread = threading.Thread(target=update_timer, args=(stop_flag, timeout))
    timer_thread.daemon = True  # checks it doesn't block program execution
    timer_thread.start()

    # Handle user input with timer
    input_thread = threading.Thread(target=get_input)
    input_thread.start()
    input_thread.join() 
    timer_thread.join()  
    return user_input

def givewordlist(num):
    if num == 1:
        return "rsrc/linuxwords.txt"
    elif num == 2:
        return "rsrc/networkingwords.txt"
    else:
        return False

