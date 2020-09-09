# ConvertPDF.py
a useful python script for converting 6 plots into one page pdf.

## Requirements for the input files
Respecting the format is very important because the computer is sensitive for the details.

- two folders
  - a folder containing plots (two speakers' three repetitions)
  - an empty folder for the generated pdfs. 
  
- plots should have their names in the format as follows
  
  **SpeakerID_stimuli number-stimuli ID_repetition.pdf**
  
  example : SIP109_01-PACV-N-1-1_1.pdf
  
- the current version is for two speaker per row, three repetition per column

  [Speaker1 repetition1] [Speaker1 repetition2] [Speaker1 repetition3]
  
  [Speaker2 repetition1] [Speaker2 repetition2] [Speaker2 repetition3]
  
**the program can be adapted to the different size, and/or number of plots, I commented which part is doing what in the program as much as I can but if it's not clear enough, don't hesitate to contact me! Always Happy to talk to Kouhais :)**
  

## How to use the script (on Mac)

- Python 3 (I tested with 3.8)

How do you know your computer has python3 ? - Open Terminal, and type `Python3`. If you see `>>>`, your computer has Python3. To get out from Python mode, you type `exit()` or control D.

- install packages 
  - type `pip install tqdm, PyPDF2, reportlab` (if `pip` doesn't work, try using `pip3` instead)
  - `tqdm`(I tested with 4.48.2) is a package for showing a progress bar while a program is running. This program takes some time, so the visualization of the process is reassuring ;)
  - `PyPDF2`(I tested with 1.26.0) is a package for merging pdfs. 
  - `reportlab`(I tested with 3.5.47) is a package for creating a textbox which can be placed on a document. 
  
- download a script
  - save a script to the appropriate place. The extention should be `.py`.  
  
- run the program
  - open Terminal
  - go to the place where the script is saved via Linux command `cd`, example `cd download/plots`
    - useful Linux commands
    - `ls` - listing the all the file names
    - `pwd` - showing the path of where you are
    
  - type `python3 convertPDF.py [the path to the folder where plots are] [the path to the destination folder]`

**Test the program with the small number of pdfs first to see if it works correctly**
sample checklists
- [ ] Is the merged file generated in the folder you want? if no, the path might be incorrect. 
- [ ] The name of the plot and the plot match? (the name of the pdf might cause this problem, it should be fixed by change the index of `pathlist`)
- [ ] The layout is what you want? if no, change the layout as you prefer. 
  
## The program doesn't work?
- read error messages, if you don't understand what it means, google it. 
- read documentations of packages.
- Google other usecases of packages.

## References
- a blog post about how to use `reportlab` (in Japanese) https://buildersbox.corp-sansan.com/entry/2020/06/09/110000
- StackExchange thread (go to Mr.Loren's sample program) https://superuser.com/questions/246092/how-to-convert-a-1-page-pdf-to-a-2-page-per-sheet-pdf/246261
- a github repo looks convenient https://github.com/nanigashi-uji/pdf_merge_multipages
  
## Alternatives
- [PDFtk](https://www.pdflabs.com/tools/pdftk-server/) seems to me an alternative for merging pdf files, though I did not try.
  
**contact : 10suism.ashida@gmail.com for any inquiries, or post me "issue" on github repository**
  
 
