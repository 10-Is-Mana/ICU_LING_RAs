# plot2pdf.py

## Expected Use Case
This program creates one page pdf with multiple plots.

## Requirements
- tqdm, PyPDF2 (install via `pip(3) install tqdm, PyPDF2`)
- the folder architecture should be as follows:
  ```
  main -- 1st row plots folder
       |- 2nd row plots folder
       |- 3rd row plots folder
       ...
  ```     
- main folder path is what Python will ask for when you run the program.
