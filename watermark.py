# read in file and watermark file
import PyPDF2
import sys
import os
import time

timestr = time.strftime("%Y%m%d-%H%M%S")

pdf_file = sys.argv[1]
watermark = sys.argv[2]

output_path = os.path.abspath(os.path.join(
    os.path.abspath(pdf_file), os.pardir))


with open(pdf_file, 'rb') as input_file, open(watermark, 'rb') as watermark_file:
    input_pdf = PyPDF2.PdfFileReader(input_file)
    watermark_pdf = PyPDF2.PdfFileReader(watermark_file)
    watermark_page = watermark_pdf.getPage(0)

    output = PyPDF2.PdfFileWriter()

    for i in range(input_pdf.numPages):
        pdf_page = input_pdf.getPage(i)
        pdf_page.mergePage(watermark_page)
        output.addPage(pdf_page)

    with open(f'{output_path}/marked_{timestr}.pdf', 'wb') as marked_file:
        output.write(marked_file)
