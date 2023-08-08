from fpdf import FPDF
  
pdf = FPDF()  

pdf.add_page()

pdf.set_font("Arial", size = 12)

f = open("./input.txt", "r")

for x in f:
    pdf.multi_cell(0, 5, txt = x) # width, height, text_content

pdf.output("gen_PDF_from_text.pdf")  
