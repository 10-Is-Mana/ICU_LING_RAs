# plot2pdf.py

## Expected Use Case
This program creates one page pdf with multiple plots (in PDF). You can specify the number of column & row. It creates plots recursively, meaning it produces pdfs until it arrives the last plot in the folder. Each pdf will be named as [the title you told Python]_0,  [the title you told Python]_1, ... 

## Requirements
- tqdm, PyPDF2 (install via `pip(3) install tqdm, PyPDF2`)

