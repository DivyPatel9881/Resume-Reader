from pathlib import Path
import re

input_folder = Path('/Resume-Reader/resumes_in_html')

def get_font_sizes(input_file_name):
    input_file_path = input_folder / input_file_name

    f = open(str(input_file_path), 'r', encoding = 'utf-8')

    text = f.read()
    f.close()

    pattern = 'font-size:[a-zA-Z0-9% ]+'
    matches = re.findall(pattern, text)

    matches = list(set(matches))

    c = 0
    for match in matches:
        index = match.find(':')
        match = match[index+1:]
        matches[c] = match.strip(' ')
        c += 1

    return matches

def get_font_families(input_file_name):
    input_file_path = input_folder / input_file_name

    f = open(str(input_file_path), 'r', encoding = 'utf-8')

    text = f.read()
    f.close()

    pattern = 'font-family:[a-zA-Z0-9-+, ]+'
    matches = re.findall(pattern, text)

    matches = list(set(matches))

    c = 0
    for match in matches:
        index = match.find(':')
        match = match[index+1:]
        matches[c] = match.strip(' ')
        c += 1
        
    return matches
