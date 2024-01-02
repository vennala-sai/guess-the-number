#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
def guessing_game():
  logo = """
    +-----------------------------------------------------------------+
    |  ,--,   .-. .-.,---.     .---.   .---.    _______ .-. .-.,---.  |
    |.' .'    | | | || .-'    ( .-._) ( .-._)  |__   __|| | | || .-'  |
    ||  |  __ | | | || `-.   (_) \   (_) \       )| |   | `-' || `-.  |
    |\  \ ( _)| | | || .-'   _  \ \  _  \ \     (_) |   | .-. || .-'  |
    | \  `-) )| `-')||  `--.( `-'  )( `-'  )      | |   | | |)||  `--.|
    | )\____/ `---(_)/( __.' `----'  `----'       `-'   /(  (_)/( __.'|
    |(__)           (__)                               (__)   (__)    |
    | .-. .-..-. .-.         ,---.   ,---.  ,---.                     |
    | |  \| || | | ||\    /| | .-.\  | .-'  | .-.\                    |
    | |   | || | | ||(\  / | | |-' \ | `-.  | `-'/                    |
    | | |\  || | | |(_)\/  | | |--. \| .-'  |   (                     |
    | | | |)|| `-')|| \  / | | |`-' /|  `--.| |\ \                    |
    | /(  (_)`---(_)| |\/| | /( `--' /( __.'|_| \)\                   |
    |(__)           '-'  '-'(__)    (__)        (__)                  |
    +-----------------------------------------------------------------+
  """
  print (logo)
  
  print("Welcome to the number guessing game!")
  print("I am thinking of a number between 1 and 100.")
  choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  attempts = 0
  if choice == 'easy':
    attempts = 10
  else:
    attempts = 5
  
  game_over = False
  answer = random.randint(1, 100)
  while attempts > 0:
    print(f"You have {attempts} remaining attempts to guess the correct number.")
    guess = int(input("Guess the number: "))
    if guess > answer:
      print("Guess too high.")
      attempts -= 1
    elif guess < answer:
      print("Guess too low.")
      attempts -= 1
    else:
      game_over = True
      print("Correct Guess. You Win!")
      break
    
  if game_over == False:
    print("Game Over! You lose.")
    print("The correct guess is: " + str(answer))

  if input("Do you want to play again? Type 'y' or 'n': ") == 'y':
    guessing_game()

guessing_game()