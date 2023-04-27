import sys
from PyPDF2 import PdfMerger

def getArgs():
    argList = sys.argv
    if(len(argList) > 1):
        argList.pop(0)
        output = argList.pop()
        mergePdf(argList, output)
    else:
        print("python main.py [pdf1.pdf] [pdf2.pdf] ... [output.pdf]")

def mergePdf(pdflist, output):
    merger = PdfMerger()
    for pdf in pdflist:
        merger.append(pdf)

    output = output+".pdf"
    merger.write(output)
    merger.close()
    print(f"Succesfully created pdf: {output}!")

getArgs()
