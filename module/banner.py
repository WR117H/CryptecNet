import os
from colorama import Fore

banner="""
    ____                  ________          __ 
   / __ \___  ___  ____  / ____/ /_  ____ _/ /_
  / / / / _ \/ _ \/ __ \/ /   / __ \/ __ `/ __/
 / /_/ /  __/  __/ /_/ / /___/ / / / /_/ / /_  
/_____/\___/\___/ .___/\____/_/ /_/\__,_/\__/  
               /_/                             
"""
def ban():
   os.system('clear||cls')
   print(Fore.LIGHTMAGENTA_EX+banner+Fore.RESET)
   
