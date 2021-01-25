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

def pdfconvert(pathlist, stimuli, tate, yoko, wdt, hgt):
    output = PdfFileWriter()
    page = pdf.PageObject.createBlankPage(None, wdt*yoko, hgt*tate)

    for i in tqdm(range(tate)):
        for j in range(yoko):
            pdf_in = PdfFileReader(pathlist[j+i*yoko])
            page.mergeScaledTranslatedPage(pdf_in.getPage(0), 1.0, wdt*j, hgt*(tate-i-1))
    output.addPage(page)
    
    with open(f'{stimuli}{".pdf"}', "wb") as f_out:
        output.write(f_out)


# path for folder
print("What is the folder path?")
path = input()
print("How many columns?")
col = int(input())
print("How many rows?")
row = int(input())
print("What is the name of the plot?")
title = input()

paths = glob.glob(path+"/*.pdf")
paths.sort()

size = col*row
n, mod = divmod(len(paths), size)
info = PdfFileReader(paths[0])
wid, high = page_info(info.getPage(0))


for k in range(n):
    pathlist = paths[k*size:(k+1)*size]
    pdfconvert(pathlist, f'{path}/{title}_{k}', row, col, wid, high)

if mod != 0:
    last = paths[n*size:]
    print(last)

    n_1, mod_1 = divmod(mod, col)
    output = PdfFileWriter()
    page = pdf.PageObject.createBlankPage(None, wid*col, high*row)

    for i in tqdm(range(n_1)):
        for j in range(col):
            pdf_in = PdfFileReader(last[j+i*col])
            page.mergeScaledTranslatedPage(pdf_in.getPage(0), 1.0, wid*j, high*(row-i-1))
    output.addPage(page)

    with open(f'{path}/{title}_{n}{".pdf"}', "wb") as f_out:
        output.write(f_out)

# left to right
# top to down
