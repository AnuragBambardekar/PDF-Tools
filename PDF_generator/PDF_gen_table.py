from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Table
from reportlab.lib import colors

def generate_pdf(output_filename):
    # Create a canvas with specified output filename and page size (letter size in this case)
    c = canvas.Canvas(output_filename, pagesize=letter)

    # Draw some text on the PDF
    c.drawString(100, 750, "Hello, this is a generated PDF!")
    c.drawString(100, 700, "Anurag Bambardekar.")
    c.drawString(100, 650, "Engineer.")
    c.drawString(100, 600, "Here are five name: Mike, Sarah, Bob, John, Emma.")
    c.drawString(100, 550, "Here are five numbers: 100,200,300,400,500.")

    # Draw a rectangle
    c.rect(100, 400, 300, 100)

    # Add a table
    data = [
        ["Name", "Age", "Occupation"],
        ["John", "30", "Engineer"],
        ["Jane", "28", "Doctor"],
        ["Tom", "35", "Teacher"],
    ]
    table = Table(data, colWidths=[100, 50, 100])
    table.setStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.wrapOn(c, 500, 200)
    table.drawOn(c, 100, 300)

    # Save the canvas (i.e., save the generated PDF)
    c.save()

if __name__ == "__main__":
    output_filename = "generated_pdf2.pdf"
    generate_pdf(output_filename)
    print(f"PDF generated successfully: {output_filename}")
