from fpdf import FPDF
  
# save FPDF() class into a variable pdf
pdf = FPDF()  
  
# Add a page
pdf.add_page()
  
# set style and size of font that you want in the pdf
pdf.set_font("Arial", size = 12)
 
# open the text file in read mode
f = open("./input.txt", "r")
 
# insert the texts in pdf using MultiCell
for x in f:
    pdf.multi_cell(0, 5, txt = x) # width, height, text_content
  
# save the pdf with name mygfg.pdf
pdf.output("gen_PDF_from_text.pdf")  
