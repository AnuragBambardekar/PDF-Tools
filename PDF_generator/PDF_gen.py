# pip install reportlab

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(output_filename):
    # Create a canvas with specified output filename and page size (letter size in this case)
    c = canvas.Canvas(output_filename, pagesize=letter)

    # Draw some text on the PDF
    c.drawString(100, 750, "Hello, this is a generated PDF!")
    c.drawString(100, 700, "Anurag Bambardekar.")
    c.drawString(100, 650, "Engineer.")

    # Draw a rectangle
    c.rect(50, 500, 300, 100)

    # Draw circles
    c.circle(100,500, 20)
    c.circle(300,500, 20, fill=1)

    # Save the canvas (i.e., save the generated PDF)
    c.save()

if __name__ == "__main__":
    output_filename = "generated_pdf.pdf"
    generate_pdf(output_filename)
    print(f"PDF generated successfully: {output_filename}")
