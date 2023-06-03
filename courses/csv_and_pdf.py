import csv
import PyPDF2
import re

pdf_path = '/home/kirill/Downloads/Find_the_Phone_Number.pdf'

data = open('/home/kirill/Downloads/find_the_link.csv')
csv_data = csv.reader(data)
link = []
for line in csv_data:
    for item in line:
        if not item.isdigit():
            link.append(item)
data.close()
f = open(pdf_path, 'rb')
pdf_reader = PyPDF2.PdfReader(f)
pdf_text = []
for i in range(len(pdf_reader.pages)):
    pdf_text.append(pdf_reader.pages[i].extract_text())
f.close()
pattern = r'\d{3}[ .-]\d{3}[ .-]\d{4}'
match = re.findall(pattern, '/n'.join(pdf_text))
print(match)
