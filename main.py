from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
# each person's name is the key, and value will be their bid
other_bids = True
bidders = []
winning_amount = 0
winner = ""

def add_bidder(name, amount):
    new_bidder = {}
    new_bidder["name"] = name
    new_bidder["amount"] = amount
    bidders.append(new_bidder)

while other_bids:
    name = str(input("Name of bidder? : "))
    bid = int(input("What is your bid amount? : $"))
    others = str(input("Are there other bidders? yes/no ")).lower()

    add_bidder(name, bid)
    

    if others == "no":
        other_bids = False
    else:
        clear()

for i in bidders:
    if i["amount"] > winning_amount:
        winning_amount = i["amount"]
        winner = i["name"]
    
print(f"The winner is {winner} with a bid of ${winning_amount}")
