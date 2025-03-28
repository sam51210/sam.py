import time
import sys

# Sam.py BootSequence
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(" ____                                                ")
print("/ ___|  __ _ _ __ ___    _ __  _   _                 ")
print("\___ \ / _` | '_ ` _ \  | '_ \| | | |                ")
print(" ___) | (_| | | | | | |_| |_) | |_| |                ")
print("|____/ \__,_|_| |_| |_(_) .__/ \__, |                ")
print("                        |_|    |___/                 ")
print("")
print("")
   

# hello :D here is your name 

name = input("What is your name? ") 

   

print("") 

time.sleep(1) # Sleep for 1 second 

print("According to my crystal ball...") 

time.sleep(3) # Sleep for 3 seconds 

print("Your name is...") 

time.sleep(3) 

  

# now we tell you your name 

print("") 

print("Hmm... is it " + name + "?") 

print("") 

  

time.sleep(1) 

truth = input("Yes (Y) or no (N)? ") 

  

if truth.upper() == 'Y': 

    print("") 

    print(f"{bcolors.OKGREEN}A magician never reveals their secrets{bcolors.ENDC}")

    time.sleep(3) 
    sys.exit()

else: 

    print("") 

    print(f"{bcolors.FAIL}I smell a liar...{bcolors.ENDC}")

    time.sleep(1) 

    print("Let's try again...") 

    time.sleep(3) 
    sys.exit()
