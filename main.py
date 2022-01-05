import art
import random

EASY_LEVEL = 10
HARD_LEVEL = 5


#function to check user's guess against actual answer  
def compare(user_guess, random_num, turn):
  """check random_num against user_guess. Returns the number of turn remaining."""
  if user_guess > random_num:
      print("Too high.")
      return turn - 1
  elif user_guess < random_num:
      print("Too low.")
      return turn - 1  
  else:
    print(f"You got it! The answer was {random_num}!") 
    print(art.win_logo) 

#function to set difficulty
def game_mode():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == 'easy':
    return EASY_LEVEL
  elif difficulty == 'hard':
    return HARD_LEVEL

def game():
  #title main screen
  print(art.logo)
  print("Welcome to the number guessing game!\n")
  print("I am thinking of a number between 1 and 100.\n")

  #choosing a random number between 1 and 100
  random_num = random.randint(0,100)

  #random number revealed for debugging
  print(f"Pssst, the correct answer is {random_num}.\n")

  #choose difficulty
  turn = game_mode()
 
  #repeat the make guess in a while loop
  user_guess = 0
  while user_guess != random_num:
    print(f"You have {turn} attempts remaining to guess the number.\n")
    #let the user guess a number
    user_guess = int(input("Make a guess: "))
    turn = compare(user_guess, random_num, turn)
    if turn == 0:
      print("You ran out of attempt, you lost!")
      print(art.lose_logo)
      return 
    elif user_guess != random_num:
      print("Guess again.")
      print(art.guess_again_logo)

game()














  
 
    
  





    


