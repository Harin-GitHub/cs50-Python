# Get fruit from the user
fruit = input("Item: ")

# Clean user input
fruit = fruit.lower().replace(" ", "")

# Make a list of fruits assosiated with their calories
calories = {
    "apple" : 130, "avocado" : 50, "banana" : 110, "cantaloupe" : 50, "grapefruit" : 60,
    "grapes" : 90, "honeydew" : 50, "melon" : 50, "kiwifruit" : 90, "lemon" : 15,
    "lime" : 20, "nectarine" : 60, "orange" : 80, "peach" : 60, "pear" : 100, "pineapple" : 50,
    "plums" : 70, "strawberries" : 50, "sweetcherries" : 100, "tangerine" : 50, "watermelon" : 80
}

# If given fruit exists print its calories
if fruit in calories:
    print(f"Calories: {calories[fruit]}")