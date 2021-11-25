import random
from replit import clear
from art import logo
def deal_card():
  """Returns a random card from deck"""
  cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Take cards and return the score"""
  if sum(cards) == 21 and len(cards)== 2:
    return 0
  if sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score,computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose"
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return " You Lose, Opponent has Blackjack"
  elif user_score == 0:
    return "You Win with a Blackjack"
  elif user_score > 21:
    return "You went over.You lose"
  elif computer_score > 21:
    return "Opponent went over. You Win"
  elif user_score > computer_score:
    return "You Win"
  else:
    return "You Lose"
def play():
  print(logo)
  user_cards=[]
  computer_cards=[]

  for _ in range (2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  game_over = False
  while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards : {user_cards}, current_score : {user_score}")
    print(f"Computer first card  : {computer_cards[0]}")


    if user_score == 0 or computer_score ==0 or user_score>21:
      game_over = True
    else:
      user_deal = input("Type 'y' to get another card or type 'n' to pass :")
      if user_deal == 'y':
        user_cards.append(deal_card())
      else:
        game_over = True

  while computer_score != 0 and computer_score< 17:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)

  print(f"Your Final Hand : {user_cards}, Final Score : {user_score}")
  print(f"Computer Final Hand : {computer_cards}, Final Score : {computer_score}")
  print(compare(user_score,computer_score))

while input("Play Game? Type 'y' or 'n' : ") == 'y' :
  clear()
  play()