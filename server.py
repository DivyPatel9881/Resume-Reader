from flask import Flask, render_template, send_from_directory, request, redirect, url_for
from secrets import token_hex

from Scripts.extractKeywords.generateCsv import *
from Scripts.convertApi.docxToPdf import *

app = Flask(__name__)

app.config['CLIENT_CSV'] = '/Resume-Reader/output_csv/'

app.config['CLIENT_DOCX'] = '/Resume-Reader/resumes_in_docx/'
app.config['CLIENT_PDF'] = '/Resume-Reader/resumes_in_pdf/'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        f = request.files['resume-file']
        print(f)
        digest = token_hex(16)
        if f.mimetype == 'application/pdf':
            pdf_file_name =  f.filename[:-4] + '_' + digest + '.pdf'
            pdf_file_path = app.config['CLIENT_PDF'] + pdf_file_name
            f.save(pdf_file_path)

            csv_file_name = f.filename[:-4] + "_" + digest + '.csv'
            csv_file_path = app.config['CLIENT_CSV'] + csv_file_name
            generate_csv(pdf_file_name, csv_file_name)

        elif f.mimetype == 'application/octet-stream':
            docx_file_name = f.filename[:-5] + '_' + digest + '.docx'
            docx_file_path = app.config['CLIENT_DOCX'] + docx_file_name
            f.save(docx_file_path)

            pdf_file_name = f.filename[:-5] + '_' + digest + '.pdf'
            docx_to_pdf(docx_file_name, pdf_file_name)

            csv_file_name = f.filename[:-5] + "_" + digest + '.csv'
            csv_file_path = app.config['CLIENT_CSV'] + csv_file_name
            generate_csv(pdf_file_name, csv_file_name)

        return send_from_directory(app.config['CLIENT_CSV'][:-1], csv_file_name, as_attachment = True)
