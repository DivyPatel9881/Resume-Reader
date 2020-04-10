from pathlib import Path
from pprint import pprint as pp
import re

input_folder = Path('/Resume-Reader/resumes_in_txt')

def get_features(input_file_name):
    input_file_path = input_folder / input_file_name

    f = open(str(input_file_path), 'r', encoding='utf-8')
    text = f.read()
    f.close()

    text = text.replace('  ', '')
    lines = text.split('\n')

    i=0
    length = len(lines)
    while(i<length):
        if(lines[i]==''):
            lines.remove(lines[i])
            length = length -1
            continue
        i = i+1

    text = '\n'.join(lines)

    return text, len(lines), len(text)

def get_emails(text):
    regex = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+)"
    matches = re.findall(regex, text)
    return matches

def get_linkedin_profiles(text):
    regex = 'linkedin.com[/a-zA-Z0-9-]+'
    matches = re.findall(regex, text)

    c = 0
    for match in matches:
        match = "https://www." + match
        matches[c] = match
        c += 1

    return matches