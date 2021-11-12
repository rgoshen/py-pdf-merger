# read in file and watermark file
import PyPDF2
import sys
import os
import time

timestr = time.strftime("%Y%m%d-%H%M%S")
output_path = os.path.abspath(os.path.join(
    os.path.abspath(sys.argv[1]), os.pardir))

input_pdf = PyPDF2.PdfFileReader(open(sys.argv[1], 'rb'))
watermark_pdf = PyPDF2.PdfFileReader(open(sys.argv[2], 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(input_pdf.numPages):
    pdf_page = input_pdf.getPage(i)
    pdf_page.mergePage(watermark_pdf.getPage(0))
    output.addPage(pdf_page)

with open(f'{output_path}/watermarked_{timestr}.pdf', 'wb') as marked_file:
    output.write(marked_file)
