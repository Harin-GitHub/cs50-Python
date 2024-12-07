def main():

    # Get user input, strip spaces and lowercase letters
    name = input("File name: ")
    name = name.lower().strip()

    # initialize list of exetensions and a variable
    i = 0
    list = [".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip"]

    # Check for file exetension
    # If found relavant break or keep repeating
    while i < 7:
        if check(name, list[i]):
            break
        else:
            i += 1
            continue

    # With the value of i when found the file's exetension print relavant file type
    match i:
        case 0:
            print("image/gif")
        case 1:
            print("image/jpeg")
        case 2:
            print("image/jpeg")
        case 3:
            print("image/png")
        case 4:
            print("application/pdf")
        case 5:
            print("text/plain")
        case 6:
            print("application/zip")
        case _:
            print("application/octet-stream")


def check(file, exe):
    """check if the given extension match with the file's itself. If match return true"""
    if file.endswith(exe):
        return True


main()