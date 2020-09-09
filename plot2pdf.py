#!/usr/bin/python
import glob
import os
import sys
from tqdm import tqdm
from PyPDF2 import PdfFileWriter, PdfFileReader, pdf

def page_info(pg_obj):
    ul=pg_obj.mediaBox.upperLeft
    dr=pg_obj.mediaBox.lowerRight
    wdt = float(dr[0]-ul[0])
    hgt = float(ul[1]-dr[1])
    return (wdt, hgt)

def pdfconvert(pathtable, stimuli, tate, yoko):
    output = PdfFileWriter()
    info = PdfFileReader(pathtable[0][0])
    wdt, hgt = page_info(info.getPage(0))

    page = pdf.PageObject.createBlankPage(None, wdt*yoko, hgt*tate)

    for i in tqdm(range(tate)):
        for j in range(yoko):
            pdf_in = PdfFileReader(pathtable[i][j])
            page.mergeScaledTranslatedPage(pdf_in.getPage(0), 1.0, wdt*j, hgt*(3-i))
    output.addPage(page)
    
    page = pdf.PageObject.createBlankPage(output)
    output.write(open(f'{stimuli}{".pdf"}', "wb"))


# path for folder
print("What is the folder path?")
path = input()
print("How many columns?")
col = int(input())
print("How many rows?")
row = int(input())
print("What is the name of the plot?")
title = input()

os.chdir(path)
path_dirs = glob.glob('*')
path_dirs.sort()
table = [[""]*col for i in range(row)]

for i in range(row):
    os.chdir(path_dirs[i])
    path_pdfs = glob.glob('*')
    path_pdfs.sort()
    for j in range(col):
        table[i][j] = f'{path_dirs[i]}/{path_pdfs[j]}'
    os.chdir("..")

#pdfconvert(table, title, row, col)
print(f'{title}.pdf is generated in the folder {path}')