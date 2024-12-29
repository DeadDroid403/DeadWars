from colorama import Fore, Style, init
import random
import time


colorslist = [
    Fore.RED,
    Fore.YELLOW,
    Fore.GREEN,
    Fore.BLUE,
    Fore.MAGENTA,
    Fore.CYAN
    ]

def logo():
    print("""

██████╗ ███████╗ █████╗ ██████╗       ██╗    ██╗ █████╗ ██████╗ ███████╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗      ██║    ██║██╔══██╗██╔══██╗██╔════╝
██║  ██║█████╗  ███████║██║  ██║█████╗██║ █╗ ██║███████║██████╔╝███████╗
██║  ██║██╔══╝  ██╔══██║██║  ██║╚════╝██║███╗██║██╔══██║██╔══██╗╚════██║
██████╔╝███████╗██║  ██║██████╔╝      ╚███╔███╔╝██║  ██║██║  ██║███████║
╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝        ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
                                                                        
        """)


def rocket():
    print("\n") 
    for i in range(60):
        time.sleep(0.020)
        print(f"{colorslist[-1]}{"~"*i}",end="")
        print(f"{colorslist[-1]}{"==>"}",end="\r")
    print("\n")
    print(Style.RESET_ALL)




