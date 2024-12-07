class Jar:
    # Initialaize attributes
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    # Return object as of the amount of cookies Jar contains
    def __str__(self):
        return f"{'🍪' * self.size}"

    # Get user input for the capacity and create a "Jar" object
    @classmethod
    def get_capacity(cls):
        capacity = input("How much capacity do you want? ")
        return cls(capacity)

    # Ask for the amount of cookies to deposit and deposit them
    def get_deposit(self):
        # Repeat asking if contain any errors
        while True:
            cookies = input("How much cookies would you like to deposit? ")
            cookies = is_valid(cookies)
            if cookies == False:
                print("Invalid deposit")
                continue
            break
        self.deposit(cookies)

    # Ask for the amount of cookies to withdraw and withdraw them
    def get_withdraw(self):
        # Repeat asking if contain any errors
        while True:
            cookies = input("How much cookies would you like to withdraw? ")
            cookies = is_valid(cookies)
            if cookies == False:
                print("Invalid withdraw")
                continue
            break
        self.withdraw(cookies)

    # Add cookies to the "Jar"
    def deposit(self, n):
        self.size += n

    # Remove cookies from "Jar"
    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        capacity = is_valid(capacity)
        while capacity == False:
            print("Invalid capacity")
            self.get_capacity()
        if capacity < 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if not 0 <= size <= self.capacity:
            raise ValueError("Invalid amount of cookies")
        self._size = size


def main():
    jar = Jar.get_capacity()
    jar.get_deposit()
    print(f"You have {jar} cookies")
    while True:
        answer = input("Do you want to deposit or withdraw cookies? (D/W) Quit(Q) ")
        match answer:
            case "D":
                jar.get_deposit()
                print(f"You have {jar} cookies")
            case "W":
                jar.get_withdraw()
                print(f"You have {jar} cookies")
            case "Q":
                exit()
            case _:
                print("Invalid answer")


def is_valid(x):
    """Return int value of a given str, return False if unable"""
    try:
        int(x)
    except ValueError:
        return False
    return int(x)


if __name__ == "__main__":
    main()
