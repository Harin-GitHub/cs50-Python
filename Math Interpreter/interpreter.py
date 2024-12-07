# Get user exspression
expression = input("Expression: ")

# Assign string values for x, y, z as of user input
x, y, z = expression.split(" ")

# Convert x and z to ints whereas y is to be operator
x = int(x)
z = int(z)

# Check y's string value
# Perform calculation matching y its real operator
match y:
    case "+":
        answer = x + z
    case "-":
        answer = x - z
    case "*":
        answer = x * z
    case "/":
        answer = x / z

# Print answer as a floating-point value
print(float(answer))