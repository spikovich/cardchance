import random

def generate_card():

    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']


    deck = [rank + ' of ' + suit for suit in suits for rank in ranks]


    chosen_card = random.choice(deck)
    return chosen_card


def is_image_card(card):
    return any(rank in card for rank in ['Jack', 'Queen', 'King'])

opponent_card = generate_card()
print("Opponent's card:", opponent_card)


cards_with_images = 12
total_cards = 52
image_card_probability = (cards_with_images / total_cards) * 100
print("Is image card:", is_image_card(opponent_card))
print("Probability of image card:",image_card_probability )
