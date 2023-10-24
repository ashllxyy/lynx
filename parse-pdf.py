import os
import PyPDF2

pdf_folder = './pdfs'

output_text_file = 'output.txt'

def extract_text_from_pdf(pdf_file, output_file):
    try:
        with open(pdf_file, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ''
            for page_number in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_number]
                text += page.extract_text()
            with open(output_file, 'a', encoding='utf-8') as out_file:
                out_file.write(text)
    except Exception as e:
        print(f"Error processing {pdf_file}: {str(e)}")

for filename in os.listdir(pdf_folder):
    if filename.endswith('.pdf'):
        pdf_file_path = os.path.join(pdf_folder, filename)
        print(pdf_file_path)
        extract_text_from_pdf(pdf_file_path, output_text_file)

print("Text extraction and concatenation completed.")
