import dealer
import addition

# function that ask user for an hit or a stand
def user_response():
  response = input("Do you want to hit or stand (type 'hit' or 'stand')? ")
  if response == 'hit':
    return response
  if response == 'stand':
    return response
  if response != 'stand' and response != 'hit':
    print("response not correct")

# function that prints our the dealers cards and the total of the cards
def full_result():
  print(f"Dealer cards are {dealer.dealer_cards} total = {addition.dealer_sum()}")
  print(f"Player cards are {dealer.player_cards} total = {addition.player_sum()}")

# function that prints out only the first card of the dealer and the player cards
def partial_result():
  print(f"Dealer first cards is {dealer.dealer_cards[0]}")
  print(f"Player cards are {dealer.player_cards} total = {addition.player_sum()}")
