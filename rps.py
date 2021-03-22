import random

computer_score = 0
user_score = 0

def user_turn():
  user_choice = input('Rock, Paper or Scissors?\n').lower()

  if user_choice=='rock' or user_choice=='paper' or user_choice=='scissors':    
    print('\nYou played %s!'%(user_choice))
    return user_choice
    print(user_choice)
  else:
    print('\nInvalid Input. Try again.')
    return user_turn()

def computer_turn():
  random_num = random.randint(0,2) 
  if random_num == 0:
    computer_choice = 'rock'
  elif random_num == 1:
    computer_choice = 'paper'
  else:
    computer_choice = 'scissors'
  
  print('PC played %s!'%(computer_choice))
  return computer_choice

def play():

  #outcome functions
  def tie():
    global computer_score
    global user_score
    print('It\'s a tie!')
    print('\nUser ---- %s X %s ---- PC\n'%(user_score, computer_score))
    play()
  
  #if user wins
  def user_wins():
    global computer_score
    global user_score
    user_score+=1
    print('\nYou Win! You are one lucky bastard hehehe')
    print('\nUser ---- %s X %s ---- PC\n'%(user_score, computer_score))
    play()
  
  #if pc wins
  def computer_wins():
    global computer_score
    global user_score
    computer_score+=1
    print('\nYou Lose! I guess chips are better than brains after all! hehehe :D')
    print('\nUser ---- %s X %s ---- PC\n'%(user_score, computer_score))
    play()

  #getting both choices
  user_choice = user_turn()
  computer_choice = computer_turn()

  #tie
  if user_choice==computer_choice:
    tie()
  #user wins
  elif (user_choice=='rock' and computer_choice=='scissors')or (user_choice=='scissors' and computer_choice=='paper') or(user_choice == 'paper' and computer_choice=='rock'):
    user_wins()
  #computer wins
  else:
    computer_wins()

play()
