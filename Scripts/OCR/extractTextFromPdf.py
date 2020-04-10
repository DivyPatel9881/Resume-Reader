from .ocrApi import *
from .cleanText import *

def extract_text_from_api(input_file_name):
    file, reader = get_pdf_reader(input_file_name)

    num_of_pages = get_number_of_pages(reader)

    text = []
    for i in range(1):
        page = get_page(reader, i)
        page_text = get_text_from_page(page)
        print(type(page_text))
        print(repr(page_text))
        print('---------------------------------------------------------------')
        # print(page_text)
        text.append(page_text)
    
    file.close()

    return clean_text(text)