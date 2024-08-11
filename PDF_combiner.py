from sys import argv
import PyPDF2
import sys
import os

# To create merger object with the PyPDF class
merger = PyPDF2.PdfMerger() 

for file in os.listdir():
    if file.endswith('.pdf'):
        merger.append(file)
        
merger.write('Combined_pdf.pdf')
