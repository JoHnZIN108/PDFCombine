from sys import argv
import PyPDF2
import sys
import os

merger = PyPDF2.PdfMerger() # To create merger object with the PyPDF class

for file in os.listdir():
    if file.endswith('.pdf'):
        merger.append(file)
        
merger.write('Combined_pdf.pdf')
