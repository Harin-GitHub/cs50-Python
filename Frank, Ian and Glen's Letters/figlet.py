import sys
import random
from pyfiglet import Figlet


n = len(sys.argv)
figlet = Figlet()
fonts = figlet.getFonts()


def main():
    if n == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":   
            if sys.argv[2] in fonts:
                process(sys.argv[2])
    elif n == 1:
        process(random.choice(fonts))

    sys.exit("Invalid usage")


def process(str_font):
    text = input("Input: ")
    figlet.setFont(font=str_font)
    print(figlet.renderText(text))
    sys.exit()