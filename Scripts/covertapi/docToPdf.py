import convertapi
from pathlib import Path

from .apiKey import *

if is_api_key_set():
    convertapi.api_secret = get_api_key()
else:
    print("Enter your API key to make conversions.")
    api_key = input()
    set_api_key(api_key)
    convertapi.api_secret = api_key

print("Found your API endpoint.")

input_folder = Path('/Resume-Reader/resumes_in_doc')
output_folder = Path('/Resume-Reader/resumes_in_pdf')

def doc_to_pdf(input_file_name, output_file_name):
    input_file_path = input_folder / input_file_name
    output_file_path = output_folder / output_file_name

    print('Converting ' + input_file_name + ' -> ' + output_file_name + ' .....' )
    result = convertapi.convert('pdf', { 'File': str(input_file_path) })
    
    result.file.save(str(output_file_path))
    print('PDF file is ready.')