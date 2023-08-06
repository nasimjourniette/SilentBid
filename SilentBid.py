import os

bidders = {}
more_bidders = True
while more_bidders:
    name = input("What is your name? ")
    while True:
        try:
            bid = input("How much would you like to bid? ")
            if bid[0] == '$' and bid[1:].isnumeric():
                pass
            else:
                raise ValueError
        except ValueError:
            print("must be an amount")
        else:
            break
    
    bidders[name] = bid
    
    while True:
        try:
            remaining = input('Are there any more bidders remaining? ').lower()
            if remaining not in ('yes', 'y', 'no', 'n'):
                raise ValueError
        except ValueError:
            print('please answer the question.')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
    if remaining in ('no', 'n'):
        more_bidders = False
    elif remaining in ('yes', 'y'):
        pass

highest_bid = 0
highest_bidder = ""

for high_bid in bidders:
    if int(bidders[high_bid][1:]) > highest_bid:
        highest_bidder = high_bid
        highest_bid = int(bidders[high_bid][1:])

print(f"{highest_bidder.title()} was the highest bidder with a bid of: ${highest_bid}.")
