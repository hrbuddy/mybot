
import PyPDF2

def getpdf():

    pdfFileObj = open('C:/Users/atul/Pictures/Chatbot/mybot/data/pdf.pdf', 'rb')

    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    pageObj = pdfReader.getPage(0)

    return pageObj.extractText()

print(getpdf())

