from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
# each person's name is the key, and value will be their bid
other_bids = True
bidding = {}

def highest_bidder(bidding_dict):
    winning_amount = 0
    winner = ""
    for b in bidding_dict:
        if bidding_dict[b] > winning_amount:
            winning_amount = bidding_dict[b]
            winner = b
    print(f"The winner is {winner} with a bid of ${winning_amount}")

while other_bids:
    name = str(input("Name of bidder? : "))
    bid = int(input("What is your bid amount? : $"))
    others = str(input("Are there other bidders? yes/no ")).lower()

    bidding[name] = bid


    if others == "no":
        other_bids = False
        highest_bidder(bidding)
    else:
        clear()
