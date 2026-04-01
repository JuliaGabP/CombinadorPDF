import pypdf
import os

# Obtém todos os nomes de arquivos PDF
pdf_filenames = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdf_filenames.append(filename)

pdf_filenames.sort(key=str.lower)

writer = pypdf.PdfWriter()

# Itera sobre todos os arquivos PDF
for pdf_filename in pdf_filenames:
    reader = pypdf.PdfReader(pdf_filename)
    # Copia todas as páginas após a primeira
    writer.append(pdf_filename, pages=(1, len(reader.pages)))

with open('combined.pdf', 'wb') as file:
    writer.write(file)
