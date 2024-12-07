import inflect


p = inflect.engine()

# Initialize a list
namelist = []

# Keep prompting user till EOF
# Add each name to the list
while True:
    try:
        name = input("Name: ")
        namelist.append(name)
    except EOFError:
        break

# Print entered name(s) correctly
print(f"Adieu, adieu, to {p.join(namelist)}")
