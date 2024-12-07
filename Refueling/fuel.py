def main():
    while True:
        frac = input("Fraction: ")
        if not convert(frac):
            continue
        else:
            percent = convert(frac)
            break
    print(gauge(percent))


def convert(fraction):
    """Take a str as input. Return equivalent percentage as int, False if met any errors"""

    # Calculate percentage using input
    x, y = fraction.split("/")
    percentage = round((int(x) / int(y)) * 100)

    # Validate
    if percentage <= 100:
        return int(percentage)
    return False


def gauge(percentage):
    """Print percentage if in range of 1%-99%. Print F if >= 99, E otherwise"""

    if percentage > 98:
        return("F")
    elif percentage < 2:
        return("E")
    else:
        return(f"{percentage}%")


if __name__ == "__main__":
    main()