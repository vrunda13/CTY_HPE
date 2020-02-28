import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io

def pdfparser(data):

    fp = open(data, 'rb')
    rsrcmgr = PDFResourceManager() #to store shared resources such as fonts or images
    retstr = io.StringIO() # Cast to StringIO object
    codec = 'utf-8'
    # Set parameters for analysis.
    laparams = LAParams()
    # Create a PDF device object
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.
    with open('G:/Pycharm/Pycharm Projects/CTYHP/t2.txt','w') as f:
        for page in PDFPage.get_pages(fp):
            interpreter.process_page(page)
            data =  retstr.getvalue()
        f.write(data)
    print("done")

if __name__ == '__main__':
    pdfparser('C:/Users/Shobha/Desktop/table.pdf')
