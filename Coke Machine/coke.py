# Initialize the value of due and a list of accepted coins
due = 50
coins = [25, 10, 5]

# Keep prompting the user until the due is equal to or lower than zero
while due > 0:

    print(f"Amount Due: {due}")
    coin = int(input("Insert Coin: "))

    # Check if a given coin is acceptable
    # If yes update the amount of due
    if coin in coins:
        due = due - coin

# Print owed money
print(f"Change Owed: {abs(due)}")