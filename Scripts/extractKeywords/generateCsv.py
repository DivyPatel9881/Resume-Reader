from pathlib import Path

from ..convertApi.pdfToTxt import *
from ..pdfToHtml.pdfToHtml import *
from .getFeatures import *
from .getHtmlFeatures import *

input_folder = Path('/Resume-Reader/resumes_in_pdf')
output_folder = Path('/Resume-Reader/output_csv')

features = ['Name', 'Phone Numbers', 'Emails', 'LinkedIn Profiles', 'Number of lines', 'Number of characters', 'Font Sizes', 'Font Families']

def generate_csv(input_file_name, output_file_name):
    # input_file_path = input_folder / input_file_name
    output_file_path = output_folder / output_file_name

    txt_file_name = input_file_name[:-4] + '.txt'
    pdf_to_txt(input_file_name, txt_file_name)

    text, lines, num_of_lines, num_of_chars = get_features(txt_file_name)

    feature_values = []
    max = 0

    # Name
    name = get_name(lines)
    feature_values.append(name)
    if max < len(name):
        max = len(name)

    #Phone numbers
    phone_numbers = get_phone_numbers(text)
    feature_values.append(phone_numbers)
    if max < len(phone_numbers):
        max = len(phone_numbers)

    #Emails
    emails = get_emails(text)
    feature_values.append(emails)
    if max < len(emails):
        max = len(emails)

    #linkedin profiles
    linkedin_profiles = get_linkedin_profiles(text)
    feature_values.append(linkedin_profiles)
    if max < len(linkedin_profiles):
        max = len(linkedin_profiles)

    feature_values.append([str(num_of_lines)])
    feature_values.append([str(num_of_chars)])

    if max < 1:
        max = 1

    html_file_name = input_file_name[:-4] + '.html'
    pdf_to_html(input_file_name, html_file_name)

    #Font sizes
    font_sizes = get_font_sizes(html_file_name)
    feature_values.append(font_sizes)
    if max < len(font_sizes):
        max = len(font_sizes)

    #Font families
    font_families = get_font_families(html_file_name)
    feature_values.append(font_families)
    if max < len(font_families):
        max = len(font_families)

    for i in range(len(feature_values)):
        print(feature_values[i])
        feature_values[i] = feature_values[i] + (['']*(max - len(feature_values[i])))
    
    f = open(str(output_file_path), 'w')

    print('Features extracted.\nGenearating CSV file...')
    csv_text = ','.join(features)

    for i in range(max):
        csv_text += '\n'
        for values in feature_values:
            csv_text += values[i] + ', '
        csv_text = csv_text[:-2]

    f.write(csv_text)
    f.close()
    print('CSV file is ready.')