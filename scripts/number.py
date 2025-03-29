elif scripto.upper() == 'NUMBER.PY':
    search("number.py","Ryan Barone")
    clear()
    
    import random

number = random.randint(1, 100)  # Computer picks a number
attempts = 0

while True:
   guess = input("Guess a number between 1 and 100: ")
   if not guess.isdigit():  # Check if input is a number
       print("Please enter a valid number.")
       continue
   guess = int(guess)
   attempts += 1
   
   if guess < number:
       print("Too low! Try again.")
   elif guess > number:
       print("Too high! Try again.")
   else:
       print(f"Congratulations! You guessed it in {attempts} tries.")
       
       end()
