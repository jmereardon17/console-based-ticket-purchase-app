TICKET_PRICE = 10
SERVICE_CHARGE = 2
tickets_remaining = 100

def calculate_price(tickets):
  return (tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:
  print("There are {} tickets remaining.".format(tickets_remaining))
  name = input("What is your name?  ")
  try:
    amount_of_tickets = int(input("Hey {}, how many tickets would you like?  ".format(name)))
    if amount_of_tickets > tickets_remaining:
      raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
  except ValueError as err:
    print("Oh no! we ran into an issue. {}. Please try again".format(err))
  else:
    amount_due = calculate_price(amount_of_tickets)
    print("Thanks {}, that would be a total of ${}".format(name, amount_due))
    should_proceed = input("Would you like to proceed {}?  (Y/N)  ".format(name))
    if should_proceed.lower() == 'y':
      # TODO: Gather credit card information and process it.
      print("SOLD!")
      tickets_remaining -= amount_of_tickets
    else:
      print("Thank you anyways, {}!".format(name))
print("Sorry the tickets are all sold out!!! :(")