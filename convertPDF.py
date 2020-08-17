# packages
import io
import glob
import os
import sys
from tqdm import tqdm
from PyPDF2 import PdfFileWriter, PdfFileReader, pdf
from reportlab.lib.colors import Color
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

# function for putting the file names
def putFileNames(page, col, row, j, pathlist):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)

    font_size = 20
    can.setFillColor(Color(0, 0, 0, alpha=1))
    can.drawString(
        col,
        float(row),
        pathlist[j]
    )

    can.save()

    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    page.mergePage(new_pdf.getPage(0))

# function for converting 6 plots to one pdf
def pdfconvert(pathlist, stimuli):
    output = PdfFileWriter()

    # obtaining info of PDF files
    page = pdf.PageObject.createBlankPage(None, 1100, 850)
    input_1 = PdfFileReader(open(pathlist[0], "rb"))
    input_2 = PdfFileReader(open(pathlist[2], "rb"))
    input_3 = PdfFileReader(open(pathlist[4], "rb"))
    input_4 = PdfFileReader(open(pathlist[1], "rb"))
    input_5 = PdfFileReader(open(pathlist[3], "rb"))
    input_6 = PdfFileReader(open(pathlist[5], "rb"))

    # layout settings
    scale = 0.7
    col1 = 15
    col2 = 15 + page.mediaBox.getWidth() * 1/3
    col3 = col2*2 - 15
    row2 = page.mediaBox.getHeight() * 1/5
    row1 = row2*3

    page.mergeScaledTranslatedPage(input_1.getPage(0), scale, col1, row1)
    page.mergeScaledTranslatedPage(input_2.getPage(0), scale, col2, row1)
    page.mergeScaledTranslatedPage(input_3.getPage(0), scale, col3, row1)
    page.mergeScaledTranslatedPage(input_4.getPage(0), scale, col1, row2)
    page.mergeScaledTranslatedPage(input_5.getPage(0), scale, col2, row2)
    page.mergeScaledTranslatedPage(input_6.getPage(0), scale, col3, row2)
    output.addPage(page)
    
    putFileNames(page, 100+col1, row1, 0, pathlist)
    putFileNames(page, 100+col1, row2, 1, pathlist)
    putFileNames(page, 100+col2, row1, 2, pathlist)
    putFileNames(page, 100+col2, row2, 3, pathlist)
    putFileNames(page, 100+col3, row1, 4, pathlist)
    putFileNames(page, 100+col3, row2, 5, pathlist)

    page = pdf.PageObject.createBlankPage(output)

    output.write(open(f'../{sys.argv[2]}/{stimuli}{".pdf"}', "wb"))

# path for folder
path = sys.argv[1]
os.chdir(path)
path_pdfs = glob.glob('*.pdf')

# such as "SIP110"
prefix = list(set([line.split("_")[0] for line in path_pdfs]))

# stimulis
f_in_set = set([line.split("_")[1] for line in path_pdfs])


for elem in tqdm(f_in_set):
    paths = []
    for i in range(1, 4):
        if f'{prefix[0]}_{elem}_{i}{".pdf"}' in path_pdfs and f'{prefix[1]}_{elem}_{i}{".pdf"}' in path_pdfs:
            paths.append(f'{prefix[0]}_{elem}_{i}{".pdf"}')
            paths.append(f'{prefix[0]}_{elem}_{i}{".pdf"}')
    if len(paths) == 6:
      pdfconvert(paths, elem)
    else:
      print(f'{elem} is not generated because there are less than 6 plots.')
