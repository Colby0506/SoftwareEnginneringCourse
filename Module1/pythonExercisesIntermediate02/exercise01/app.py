from BankAccount import BankAccount

# Instantiate a BankAccount with a hardcoded account_name and starting_balance
account = BankAccount("John Doe", 1000)

# Deposit some amount
account.deposit(500)

# Withdraw some amount
account.withdraw(200)

# Print the balance using get_balance method
print(account.get_balance())