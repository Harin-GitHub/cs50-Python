from fpdf import FPDF, Align


class PDF(FPDF):
    def header(self):
        """Create header 'CS50 Shirtificate'"""

        # Set cursor at 3cm from top, adjust font
        self.set_y(30)
        self.set_text_color(15, 15, 15)
        self.set_font("helvetica", "", 48)

        # Print string in a cell, center cell horizontally
        self.cell(None, None, "CS50 Shirtificate", center=True)


def main():
    # Ask for the name of user
    name = input("Name: ")

    # Create an object of class "PDF", add a new page
    pdf = PDF()
    pdf.add_page()

    # Add the header
    pdf.header()

    # Place the image
    pdf.image(
        "https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png",
        x=Align.C,
        y=70,
        w=190,
    )

    # Print string on the shirt
    pdf.set_y(132)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", "", 24)

    pdf.cell(None, None, f"{name} took CS50", center=True)

    # Output pdf type file
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
