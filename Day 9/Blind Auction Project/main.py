import art
print(art.logo)
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
bid_dict = {}
continue_bid = True

def find_highest_bidder(bidding_dictionary):

    highest_bid = 0
    highest_bidder = ""

    for bidder in bid_dict:
        if bid_dict[bidder] > highest_bid:
            highest_bid = bid_dict[bidder]
            highest_bidder = bidder
    print(f"highest is from {highest_bidder} with bid: {highest_bid}")

while continue_bid:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $ "))
    bid_dict[name] = price

# TODO-3: Whether if new bids need to be added
    another_bid = input("Is there another bid? (yes/no) ").lower()
    if another_bid == "no":
        continue_bid = False
        find_highest_bidder(bid_dict)
    else:
        print("\n" * 20)
# TODO-4: Compare bids in dictionary


