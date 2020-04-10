import PyPDF2
from pathlib import Path

input_folder = Path('/Resume-Reader/resumes_in_pdf')

def get_pdf_reader(input_file_name):
    input_file_path = input_folder / input_file_name
    pdfFileObj = open(str(input_file_path), 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    return pdfFileObj, pdfReader

def get_number_of_pages(reader):
    return reader.numPages

def get_page(reader, n):
    return reader.getPage(n)

def get_text_from_page(page):
    return page.extractText()