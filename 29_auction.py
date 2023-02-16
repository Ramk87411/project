
print("Welcome to Blind auction Biding: ")

continue_bidding = False

bidding = {}

def highest_bidder(bidding_record):
    highest_bidder = 0
    winner = ""
    for bidders in bidding_record:
        bid_amount = bidding_record[bidders]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bidders
            
    print(f"The winnner is {winner} with a bid of {highest_bidder}")
            
            
while not continue_bidding:
    name = input("Please enter your name: \n")
    bid_amount = int(input("Enter your Bid amount $: \n"))
    bidding[name] = bid_amount
    continue_bid = input("Should we continue bidding: types 'Yes' or 'No'")
    if continue_bid == "no":
        continue_bidding = True
        highest_bidder(bidding)
    # elif continue_bidding == "yes":
    


