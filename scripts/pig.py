if scripto.upper() == 'PIG.PY': # Sampyhub Exclusive
    search("pig.py","Daniel Schroeder") # Sampyhub Exclusive
    clear() # Sampyhub Exclusive
    
    from random import randint


def check_die(score, die_value):
    if die_value == 1:
        return 0
    else:
        return score + die_value


def display_scoreboard(player_score, computer_score):
    print()
    print("#" * 20)
    print(f"Player Score: {player_score}")
    print(f"Computer Score: {computer_score}")
    print("#" * 20)
    print()


player_score = 0
computer_score = 0

welcome_message = """
          Welcome to 'Pig', a dice game!
    
    In this game, a user and a computer opponent 
    roll a 6-sided die each round. If the value of
    the die is a 1, the player that rolled the 1 loses
    all of their points. Otherwise, the player gets the
    value of the die added to their points. The first
    player to reach 30 points wins!
"""

print(welcome_message)

username = input("What is your name? ")

while True:
    input(f"Press 'Enter' to roll the die {username}!\n")

    player_die_value = randint(1, 6)
    print(f"{username} rolls a {player_die_value}")

    computer_die_value = randint(1, 6)
    print(f"Computer rolls a {computer_die_value}")

    player_score = check_die(player_score, player_die_value)
    computer_score = check_die(computer_score, computer_die_value)

    display_scoreboard(player_score, computer_score)

    if player_score >= 30:
        print(f"{username} wins!")
        break
    elif computer_score >= 30:
        print("Computer wins!")
        break
    
end() # Sampyhub Exclusive
