from fpdf import FPDF


def main():
    name = input("Name: ")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 9)
    pdf.cell(33, -10, 'CS50 Shirtificate', align='C')
    pdf.image("https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png", 10, 10, 33)
    pdf.set_font("helvetica", "B", 4)
    pdf.set_text_color(255)
    pdf.cell(-33, 25, f"{name} took CS50", new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.output("Shirtificate.pdf")


if __name__ == "__main__":
    main()