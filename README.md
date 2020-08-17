# ConvertPDF.py
a useful python script for converting 6 plots into one page pdf.

## Requirements for the input files
Respecting the format is very important because the computer is sensitive for the details.

- the two folders
  - a folder containing plots (two speakers' three repetitions)
  - an empty folder for the generated pdfs.
  
- the plots should have their names in the format as follows
  
  **SpeakerID_stimuli number-stimuli ID_repetition.pdf**
  
  example : SIP109_01-PACV-N-1-1_1.pdf
  
- the current version is for two speaker per row, three repetition per column

  [Speaker1 repetition1] [Speaker1 repetition2] [Speaker1 repetition3]
  
  [Speaker2 repetition1] [Speaker2 repetition2] [Speaker2 repetition3]
  


## How to use the script

- Python 3 (preferably 3.8)

How do you know your computer has python3 ? - Open Terminal, and type `Python3`. If you see `>>>`, your computer has Python3. To get out from Python mode, you type `exit()` or command D.

- Install packages 
  - type `pip install tqdm, PyPDF2, reportlab` (if `pip` doesn't work, try using `pip3` instead)
  

- download a script
  - download a script to the appropriate place 
  
- run the program
  - open Terminal
  - go to the place where the script is downloaded by using Linux command `cd`, example `cd download/plots`
    - useful Linux commands
    - `ls` - listing the all the file names
    - `pwd` - showing the path of where you are
    
  - type `python3 convertPDF.py [the path to the folder where plots are] [the path to the destination folder]`
  
  
 
