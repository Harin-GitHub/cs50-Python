# Initialize total to zero and a dict of menu
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0

# Reprompt the user, if item is found in menu update total
# If user ctrl+d quit program
while True:
    try:
        item = input("Item: ").strip().title()
        if item in menu:
            total += menu[item]
            print(f"Total: ${total:.2f}")
    except EOFError:
        break
print()