# /usr/bin/python3
# -*- coding: utf-8 -*-
"""
author: He xiaoming
2019-11-18
"""
from PyPDF2 import PdfFileReader, PdfFileWriter

infn = "1.pdf"
pdf_input = PdfFileReader(open(infn, 'rb'))
page_count = pdf_input.getNumPages()
pdf_output = PdfFileWriter()
