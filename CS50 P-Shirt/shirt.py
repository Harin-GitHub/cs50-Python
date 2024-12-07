import sys
import os
from PIL import Image, ImageOps


def main():
    # Check if user input 3 arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        # Determine extensions of the inputs
        for i in [1, 2]:
            path = os.path.splitext(sys.argv[i])
            exe = path[1].lower()

            # Check if the extensions of two inputs are valid
            if exe in [".jpg", ".jpeg", ".png"]:
                # Exit if both arguments are not in same exetension
                if i == 1:
                    extension = exe
                else:
                    if not exe == extension:
                        sys.exit("Input and output have different extensions")
            elif i == 1:
                sys.exit("Invalid input")
            else:
                sys.exit("Invalid output")

    # Open image of "shirt.png"
    shirt = Image.open("shirt.png")

    try:
        subject = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    # Overlay the 2nd image with "shirt"
    # Save
    image = overlay(shirt, subject)
    image.save(sys.argv[2])


def overlay(image1, image2):
    """Take two images. Overlay second with first. Return the overlayed image"""
    image2 = ImageOps.fit(image2, size=image1.size)
    image2.paste(image1, image1)
    return image2


if __name__ == "__main__":
    main()
