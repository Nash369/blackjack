import dealer

# add all the cards of the dealer
def dealer_sum():
  dealer_total = 0
  for i in dealer.dealer_cards:
    dealer_total += i
    # remove 11 if total card is greater than 21
  if dealer_total > 21 and 11 in dealer.dealer_cards:
    dealer.dealer_cards.remove(11)
    dealer.dealer_cards.append(1)
    dealer_sum()
  # return the total
  return dealer_total

# add all the cards of the player
def player_sum():
  player_total = 0
  for i in dealer.player_cards:
    player_total += i
  # remove 11 if total card is greater than 21
  if player_total > 21 and 11 in dealer.player_cards:
    dealer.player_cards.remove(11)
    dealer.player_cards.append(1)
    player_sum()
  # return the total
  return player_total
