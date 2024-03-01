class Category:
  # Function that creates a new object when it is called
  ## Including the name of the account, the total balance
  ## and the ledger with all transactions
  def __init__(self, name):
    self.name = name
    self.ledger = []
    self.total_ballance = 0.0
    
  # Adds an amount and description if given, to the ledger
  def deposit(self, amount, description=""):
    self.total_ballance += amount
    self.ledger.append({"amount": amount, "description": description})

  # Withdraws an amount and description if given, from the ledger
  ## If there is not enough money, nothing is added to the ledger
  def withdraw(self, amount, description=""):
    
    if self.check_funds(amount):
      self.total_ballance += -amount
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      print("Insufficient funds.")
      return False
      
  # Simple call to the total balance variable 
  def get_balance(self):
    return self.total_ballance

  # Transfers an amount from one account to another
  def transfer(self, amount, account):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + account.name)
      account.deposit(amount, "Transfer from " + self.name)
      return True
    else:
      print("Transfer failed.")
      return False

  # Simple check if 
  def check_funds(self, amount):
    if amount > self.total_ballance:
      return False
    else:
      return True
  
  # The receipt creator     
  def __str__(self):
    # Title line
    title = f"{self.name.center(30, '*')}\n"

    # Ledger items
    items = ""
    for item in self.ledger:
      description = item['description'][:23].ljust(23)
      amount = format(item['amount'], '.2f').rjust(7)
      items += f"{description}{amount}\n"
  
    #Category total
    total = f"Total: {self.get_balance():.2f}"
  
    return title + items + total
  
# The chart maker
def create_spend_chart(categories):
  # Calculate the total withdrawals for each category
  total_withdrawals = [sum(transaction['amount'] for transaction in category.ledger if transaction['amount'] < 0)
                       for category in categories]

  # Calculate the percentage spent for each category
  total_spent = sum(total_withdrawals)
  percentages = [(amount / total_spent) * 100 for amount in total_withdrawals]

  # Round down the percentages to the nearest 10
  rounded_percentages = [int(percent // 10) * 10 for percent in percentages]

  # Build the chart string
  chart = "Percentage spent by category\n"
  for i in range(100, -1, -10):
      line = str(i).rjust(3) + "| "
      for percentage in rounded_percentages:
          if percentage >= i:
              line += "o  "
          else:
              line += "   "
      chart += line + "\n"

  # Add horizontal line and category names
  chart += "    " + "-" * (3 * len(categories) + 1) + "\n"
  max_length = max(len(category.name) for category in categories)
  for i in range(max_length):
      line = "     "
      for category in categories:
          if i < len(category.name):
              line += category.name[i] + "  "
          else:
              line += "   "
      chart += line
      if i < max_length - 1:
          chart += "\n"

  return chart

print(create_spend_chart([Account_1, Account_2]))


# Failed:create_spend_chart should print a different chart representation. Check that all spacing is exact.
# Failed:The withdraw method should return False if the withdrawal didn't take place.
# Failed:Calling the withdraw method with no description should create a blank description.
# Failed:The withdraw method should return True if the withdrawal took place.
# Failed:Calling the deposit method with no description should create a blank description.
