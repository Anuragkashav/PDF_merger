from flask import Blueprint, render_template, request, send_file
import PyPDF2

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/merge', methods=['POST'])
def merge_pdfs():
    uploaded_files = request.files.getlist('pdf_files')
    merger = PyPDF2.PdfFileMerger()
    
    for file in uploaded_files:
        if file.filename.endswith('.pdf'):
            merger.append(file)

    output_path = 'app/static/combined.pdf'
    merger.write(output_path)
    merger.close()

    return send_file(output_path, as_attachment=True)
