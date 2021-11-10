import art
import dealer
import addition
import question
##import replit

# This function compares the cards of the dealer and the player
def compare_result(dealer_cards,player_cards):
  if dealer_cards ==21 and player_cards== 21:
    question.full_result()
    print("Its a tie")
  elif dealer_cards == 21:
    question.full_result()
    print("Dealer has a blackjack. You lose ☹")
  elif player_cards== 21:
    question.full_result()
    print("You have a blackjack. You win 🎉")
  elif player_cards> 21:
    question.full_result()
    print("Busted, You lose ☹")
  elif dealer_cards >21:
    question.full_result()
    print("Dealer is Busted. You win 🎉")
  elif dealer_cards > player_cards:
    question.full_result()
    print("Dealer Wins")
  elif player_cards>dealer_cards:
    question.full_result()
    print("You win 🎉")

# This is the  start of the main game
def mygame():
  # print the logo and deal the first two cards
  print(art.logo)
  for i in range(2):
      dealer.deal_cards()
  question.partial_result()

  # game_on variable is set to know when the user finish a round in the game
  game_on = True
  # keep dealing cards until the user types stand
  while True:
    response = question.user_response()
    if response == "hit":
      dealer.deal_cards()
      question.partial_result()
      print()
    
    # if the user types stand stop dealing cards and makesure dealer card is more than 17
    elif response == "stand":
      while addition.dealer_sum() < 17:
          dealer.draw_card()
      # compare the card of both the dealer and the player
      compare_result(addition.dealer_sum(),addition.player_sum())
      game_on = False
    
    # ask the user if he wants to play again
    if game_on == False:
      play_again = input("Do you want to play again(type 'yes' or 'no')? ")
      if play_again == "no":
        break
      else:
        replit.clear()
        dealer.dealer_cards = []
        dealer.player_cards = []
        mygame()

# start game
mygame()
