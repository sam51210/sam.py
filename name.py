import time

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

print("__        __   _                            _        ")
print("\ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___  ")
print(" \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \ ")
print("  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |")
print(" __\_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/ ")
print("/ ___|  __ _ _ __ ___    _ __  _   _                 ")
print("\___ \ / _` | '_ ` _ \  | '_ \| | | |                ")
print(" ___) | (_| | | | | | |_| |_) | |_| |                ")
print("|____/ \__,_|_| |_| |_(_) .__/ \__, |                ")
print("                        |_|    |___/                 ")
print("")
print("Sam.py Status:")
print(f"{bcolors.WARNING}WARN (Sam.py Hub not installed){bcolors.ENDC}")
print("")
print("Script selected:")
print(f"{bcolors.BOLD}name.py{bcolors.ENDC}")
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

    print("A magician never reveals their secrets...") 

    time.sleep(3600) 

else: 

    print("") 

    print("I smell a liar...") 

    time.sleep(1) 

    print("Let's try again...") 

    time.sleep(3600) 