import re

from .findAll import *

aggregation_of_special_charaters = '#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'
aggregation_of_normal_characters = 'a-zA-Z0-9'
aggregation_of_expected_characters = aggregation_of_normal_characters + aggregation_of_special_charaters

def clean_text(pages_text):

    pattern = re.compile('['+aggregation_of_expected_characters+']\n | \n['+aggregation_of_expected_characters+']|['+aggregation_of_expected_characters+']\n['+aggregation_of_expected_characters+']')

    c = 0
    for text in pages_text:
        matches = find_all(pattern, text)
        for match in matches:
            new_str = match.replace('\n','')
            text = text.replace(match, new_str)
        pages_text[c] = text
        c += 1
    
    return pages_text
