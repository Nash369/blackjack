import random
# create empty lists that will hold the card of the dealer and the players
dealer_cards = []
player_cards = []

# function that add a card to the list
def deal_cards():
  dealer_cards.append(random.randint(1,11))
  player_cards.append(random.randint(1,11))

# function that add a card only to the dealer cards list
def draw_card():
  dealer_cards.append(random.randint(1,11))
