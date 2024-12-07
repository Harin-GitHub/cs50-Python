# Take user input, check for errors
# If any, reprompt
while True:
    fraction = input("Fraction: ")
    try:

        # Calculate percentage using input
        x, y = fraction.split("/")
        percentage = round((int(x) / int(y)) * 100)

    except (ValueError, ZeroDivisionError):
        pass

    # Validate
    else:
        if percentage <= 100:
            break

# Print percentage if in range of 1%-99%
# Print F or E if >= 99, <= 1
if percentage > 98:
    print("F")
elif percentage < 2:
    print("E")
else:
    print(f"{percentage}%")
