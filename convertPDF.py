# packages required
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
    """
    
    page :: page obeject
    col, row :: column and row index
    j :: index for pathlist
    pathlist :: a list of the 6 pdf files' path
    
    """
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    
    # you can change font_size and font, by codes such as below.
    # font_size = 10
    # can.setFont("Times-Roman", font_size)
    can.setFillColor(Color(0, 0, 0, alpha=1))
    
    # specifying (width, height, string). without float() it doesn't work (maybe because I used the ratio?).
    can.drawString(col, float(row), pathlist[j])

    can.save()

    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    page.mergePage(new_pdf.getPage(0))

# function for converting 6 plots to one pdf
def pdfconvert(pathlist, stimuli):
    """
    
    pathlist :: a list contains 6 pdfs' paths
    stimuli :: stimuli number
    
    """
    output = PdfFileWriter()

    # obtaining info of PDF files
    # creating a blank page object (None, width, height)
    page = pdf.PageObject.createBlankPage(None, 1100, 850)
    
    # reading pdf files
    input_1 = PdfFileReader(open(pathlist[0], "rb"))
    input_2 = PdfFileReader(open(pathlist[2], "rb"))
    input_3 = PdfFileReader(open(pathlist[4], "rb"))
    input_4 = PdfFileReader(open(pathlist[1], "rb"))
    input_5 = PdfFileReader(open(pathlist[3], "rb"))
    input_6 = PdfFileReader(open(pathlist[5], "rb"))

    # page settings - changing the value here to adjust 
    # the bottom left corner is (0, 0)
    # scaling of each plot
    scale = 0.7
    # width
    col1 = 15
    col2 = 15 + page.mediaBox.getWidth() * 1/3
    col3 = col2*2 - 15
    # height
    row2 = page.mediaBox.getHeight() * 1/5
    row1 = row2*3

    # layout - which place to put which plot (page.getPage(0), scale, width, height)
    page.mergeScaledTranslatedPage(input_1.getPage(0), scale, col1, row1)
    page.mergeScaledTranslatedPage(input_2.getPage(0), scale, col2, row1)
    page.mergeScaledTranslatedPage(input_3.getPage(0), scale, col3, row1)
    page.mergeScaledTranslatedPage(input_4.getPage(0), scale, col1, row2)
    page.mergeScaledTranslatedPage(input_5.getPage(0), scale, col2, row2)
    page.mergeScaledTranslatedPage(input_6.getPage(0), scale, col3, row2)
    output.addPage(page)
    
    # putting file names (page, width, height, index, list)
    putFileNames(page, 100+col1, row1, 0, pathlist)
    putFileNames(page, 100+col1, row2, 1, pathlist)
    putFileNames(page, 100+col2, row1, 2, pathlist)
    putFileNames(page, 100+col2, row2, 3, pathlist)
    putFileNames(page, 100+col3, row1, 4, pathlist)
    putFileNames(page, 100+col3, row2, 5, pathlist)

    # creating an output as pdf
    page = pdf.PageObject.createBlankPage(output)

    output.write(open(f'../{sys.argv[2]}/{stimuli}{".pdf"}', "wb"))

# path for folder
path = sys.argv[1]
os.chdir(path)
# this obtains all the pdf file names
path_pdfs = glob.glob('*.pdf')

# such as "SIP110"
prefix = list(set([line.split("_")[0] for line in path_pdfs]))

# stimuli
f_in_set = set([line.split("_")[1] for line in path_pdfs])

# using tqdm to show the progress bar
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
