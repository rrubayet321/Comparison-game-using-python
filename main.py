
#Print the logo
from art import logo, vs
from random import choice
from game_data import data
from replit import clear
print(logo)

#Function that formats the print statement according to the correct order.
def format(item):
  """This function your random dictionary into a formatted statement"""
  item_name= item["name"]
  item_decrip= item["description"]
  item_country= item["country"]
  return f"{item_name}, a {item_decrip}. from {item_country}."

def compare(flr_a,ask,flr_b):
  """This function helps you to compare the users guess and the actual answer"""
  if flr_a > flr_b:
    if ask=="a":
      return True
    else:
      return False
  else:
    if ask=="b":
      return True
    else:
      return False
    


#Import random and randomly select two items from the game data and store them to two different variable.
game_continue= True
item_b= choice(data)
while game_continue: #This while loop will allow the user to keep on making guesses until they're wrong.

  item_a= item_b #To replace item B at item A after each comparison.
  item_b= choice(data)
  while item_a== item_b:
    item_b= choice(data)
  
  print(f"Compare A: {format(item_a)}")
  
  #Print the versus logo
  print(vs)
  
  print(f"Against B: {format(item_b)}")
  
  
  
  #Ask a user to make a guess.
  ask= input("Hey user who has more followers? A or B -  ").lower()
  score=0 #Using this variable to keep track of the score
  #Function in which the comparison occurs between followers
  flr_a= item_a["follower_count"]
  flr_b= item_b["follower_count"]
  
  correct_flag = compare(flr_a, ask, flr_b)
  clear() #This clears the screen after each guess
  print(logo) #To look good I've printed the logo
  
  if correct_flag:
    score+=1 #Keeping track of the score and letting the user know.
    print(f"You guessed it correct! Your score is {score}")
  else:
    game_continue= False
    print(f"Wrong answer! Your final score is {score}")
    
    
  
  

  


