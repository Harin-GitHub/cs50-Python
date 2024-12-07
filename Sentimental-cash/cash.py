from cs50 import get_float


while True:
    # Get user input
    owed_dollars = get_float("Change owed: ")

    # Convert dollars into cents
    owed = int(owed_dollars * 100)

    # Validating
    if owed < 0:
        continue
    else:
        break

# Initializing coin count to zero
count = 0

# Check for largest coin or coins of value
# substract the value from owed money
# update count
while owed >= 25:
    owed -= 25
    count += 1
while owed >= 10:
    owed -= 10
    count += 1
while owed >= 5:
    owed -= 5
    count += 1
while owed >= 1:
    owed -= 1
    count += 1

# Print minimum number of coins for owed
print(count)
