import PyPDF2
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/merge', methods=['POST'])
def merge_pdfs():
    uploaded_files = request.files.getlist('pdf_files')
    merger = PyPDF2.PdfFileMerger()
    
    for file in uploaded_files:
        if file.filename.endswith('.pdf'):
            merger.append(file)

    output_path = 'static/combined.pdf'
    merger.write(output_path)
    merger.close()

    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

