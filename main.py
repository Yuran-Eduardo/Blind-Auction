from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
type = True 

def highest_bind(bidding_record):

  highest_paid = 0
  for bidder in bidding_record:

    bid_amount = bidding_record[bidder]
    if bid_amount > highest_paid:
      highest_paid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_paid}")
           
while type:
  
  name = input("What's your name?")
  amount = int(input("How much do you want invest $"))
  user = {}
  user[name] = amount
  
  result = input("Are there any other Bidders? type yes to add and no end/n").lower()
  if result == "no":
    type = False 
  elif result == "yes":
    clear()

highest_bind(user)