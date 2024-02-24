import os, art

# Clearing the Screen
os.system('cls')

print(art.logo)

next_user = True
bid_dict ={}
sorted_bid_dict ={}
while next_user == True:
    user_name = input("What is your name?")
    user_bid = int(input("What's your bid?"))
    bid_dict.update(({user_name:user_bid}))
    other_bidder = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if other_bidder == 'no':
        next_user = False
    os.system('cls')
sorted_bid_dict = dict(sorted(bid_dict.items(), key = lambda x:x[1]))
print(bid_dict)
print(sorted_bid_dict)
print(len(sorted_bid_dict))
last_value = list(sorted_bid_dict.values())[-1]
print(last_value)