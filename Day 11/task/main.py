import art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def get_cards(number_of_cards):
    number_list = []
    for i in range(number_of_cards):
        card = random.choice(cards)
        number_list.append(card)
    return number_list

def black_jack():
    print(art.logo)
    play_game = input("Do you want to play a game of Black Jack? type 'y' or 'n': ")
    while play_game == "y":
        player_hand = 0
        bank_hand = 0

        cards_list = get_cards(number_of_cards=2)

print(random.choice(cards))

# ToDo Pull 2 cards and display, calculate amount
# ToDo Pull 1 card for computer and display
# ToDo Get another card or pass
# ToDo pull another card and update display and amount
# ToDo If above 21 lose
# ToDo Create computer pull amount and display
# ToDo Win conditions
# ToDo play again y/n
# black_jack()