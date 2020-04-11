import os
from pathlib import Path

input_folder = Path('/Resume-Reader/resumes_in_pdf')
output_folder = Path('/Resume-Reader/resumes_in_html')

script_file_path = Path('/Resume-Reader/Scripts/pdfToHtml/pdf2Txt.py')

def pdf_to_html(input_file_name, output_file_name):
    input_file_path = input_folder / input_file_name
    output_file_path = output_folder / output_file_name
    
    command = 'python ' + str(script_file_path) +' -o ' + str(output_file_path) + ' -t html ' + str(input_file_path)

    print('Converting ' + input_file_name + ' -> ' + output_file_name + ' .....' )
    os.system(command)
    print('HTML file is ready.')