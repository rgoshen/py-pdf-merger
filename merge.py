import PyPDF2
import sys
import time

timestr = time.strftime("%Y%m%d-%H%M%S")

input_files = sys.argv[1:]


def pdf_merge(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(f'merged_{timestr}.pdf')
    print('all files merged')


pdf_merge(input_files)
