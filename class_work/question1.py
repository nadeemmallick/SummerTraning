def withdraw_money(account_balance, amount):
    if amount <= 0:
        return "Invalid amount. Please enter a positive value."
    elif amount > account_balance:
        return "Insufficient funds."
    else:
        account_balance -= amount
        return f"Withdrawal successful. New balance: ${account_balance}"

try:
    balance = float(input("Enter your current account balance: $"))
    withdraw_amount = float(input("Enter amount to withdraw: $"))

    result = withdraw_money(balance, withdraw_amount)
    print(result)

except ValueError:
    print("Please enter valid numeric values.")