import PyPDF2 as pdf
from PyPDF2 import PdfReader, PdfWriter

# print(dir(pdf))
"""
['DocumentInformation', 'PageObject', 'PageRange', 'PaperSize', 'PasswordType', 'PdfFileMerger', 'PdfFileReader', 'PdfFileWriter', 
'PdfMerger', 'PdfReader', 'PdfWriter', 'Transformation', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', 
'__name__', '__package__', '__path__', '__spec__', '__version__', '__warningregistry__', '_cmap', '_codecs', '_encryption', '_merger', 
'_page', '_protocols', '_reader', '_security', '_utils', '_version', '_writer', 'constants', 'errors', 'filters', 'generic', 'pagerange', 
'papersizes', 'parse_filename_page_ranges', 'types', 'warnings', 'xmp']
"""

# Reading a PDF file
file = open("./sample.pdf","rb")

reader = PdfReader(file)

# Get metadata of PDF doc
info = reader.metadata
# print(info)

# Get number of pages
num_pages = len(reader.pages)
# print(num_pages)

# extract text
text = reader.pages[1].extract_text()
# print(text)

# Function to get metadata
def get_pdf_metadata(pdf_file_path):
    with open(pdf_file_path, "rb") as f:
        reader = PdfReader(f)
        info = reader.metadata
    return info

print(get_pdf_metadata("./sample.pdf"))

# Function to get text from PDF
def get_text_from_pdf(pdf_file_path):
    with open(pdf_file_path, "rb") as f:
        reader = PdfReader(f)
        results = []
        for i in range(0, len(reader.pages)):
            text = reader.pages[i].extract_text()
            results.append(text)
    return "".join(results)

print(get_text_from_pdf("./sample.pdf"))