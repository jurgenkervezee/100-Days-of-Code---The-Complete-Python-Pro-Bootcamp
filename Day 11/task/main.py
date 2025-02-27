import art, random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
get_another_card = ""

def get_cards(number_of_cards, score_dict):
    for i in range(number_of_cards):
        card = random.choice(cards)
        score_dict["cards"].append(card)
    score_dict = calculate_cards(score_dict)
    return score_dict

def calculate_cards(score_dict):
    deck_amount = 0
    for card in score_dict["cards"]:
        deck_amount +=  card
    score_dict["score"] = deck_amount
    return score_dict

def display_cards_and_score(score_dict, phase):
    cards_in_hand = score_dict["cards"]
    current_score = score_dict["score"]
    if phase == "player_setup":
        print(f"Your cards: {cards_in_hand}, current score: {current_score}")

    elif phase == "computer_setup":
        show_single_card = score_dict["cards"][0]
        print(f"computer first card: {show_single_card}")

    elif phase == "player_final":
        print(f"Your final cards: {cards_in_hand}, final score: {current_score}")

    elif phase == "computer_final":
        print(f"computers final cards: {cards_in_hand}, final score: {current_score}")

def calculate_winner(final_score_player, final_score_computer):

    calculate_final_score(final_score_player)
    calculate_final_score(final_score_computer)

    display_cards_and_score(final_score_player, "player_final")
    display_cards_and_score(final_score_computer, "computer_final")

    if final_score_computer["score"] > final_score_player["score"] and final_score_computer["score"] < 22:
        print("Computer wins, you lose")
    elif final_score_player["score"] > final_score_computer["score"] and final_score_player["score"] < 22:
        print("You win")
    elif final_score_player["score"] == final_score_computer["score"] and final_score_player["score"] < 22:
        print("Draw!")
    else:
        print("You both lose")

def calculate_final_score(final_score):
    if final_score["score"] > 21:
        for i in range(len(final_score["cards"])):
         if final_score["cards"][i] == 11:
             final_score["cards"][i] = 1
         calculate_cards(final_score)

def black_jack():
    play_game = input("Do you want to play a game of Black Jack? type 'y' or 'n': ").lower()
    while play_game == "y":

        score_player = { "cards": [],
                         "score": 0 }
        score_computer = { "cards": [],
                           "score": 0 }

        print(art.logo)
        get_cards(number_of_cards=2, score_dict = score_player)
        get_cards(number_of_cards=2, score_dict = score_computer)
        display_cards_and_score(score_player, "player_setup")
        display_cards_and_score(score_computer,  "computer_setup")

        continue_player_phase = True
        while continue_player_phase:

            get_another_card = input("Type 'y' to get another card, type 'n to pass: ").lower()
            if get_another_card == "y":
                get_cards(number_of_cards=1, score_dict = score_player)
                display_cards_and_score(score_player, "player_setup")
                display_cards_and_score(score_computer,  "computer_setup")

                if score_player["score"] > 21:
                    continue_player_phase = False
                    calculate_winner(score_player, score_computer)

            elif get_another_card == "n":
                while score_computer["score"] <= 16:
                    get_cards(number_of_cards=1, score_dict = score_computer)
                calculate_winner(score_player, score_computer)
                continue_player_phase = False

        play_game = input("Do you want to play a game of Black Jack? type 'y' or 'n': ").lower()
        score_player.clear()
        score_computer.clear()

black_jack()
