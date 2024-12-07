# Initialize an empty dict
groc_list = {}

# Reprompt the user for input, if control-d break from loop
while True:
    try:
        item = input().strip().upper()

        # If item does not exist in dict, update
        # If does, update count
        if item not in groc_list:
            groc_list.update({item : 1})
        else:
            groc_list[item] += 1
    except EOFError:
        break

# Show the grocery list
for item in sorted(groc_list):
    print(f"{groc_list[item]} {item}")