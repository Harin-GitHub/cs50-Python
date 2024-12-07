import validators


# Get user email, check whether valid or not
is_valid = validators.email(input("What's your email address? "))

# Print output as of validity
if is_valid:
    print("Valid")
else:
    print("Invalid")
