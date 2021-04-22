import pyttsx3 as pt
import pdfplumber as pd
import PyPDF2 as y
file = 'my_pdf.pdf'
f=open(file,'rb')
pdfR=y.PdfFileReader(f)
pages=pdfR.numPages
#print (pages)
with pd.open(file) as pdf:
    for i in range(0,pages):
        page=pdf.pages[i]
        text=page.extract_text()
        print(text)
        speaker=pt.init()
        speaker.say(text)
        speaker.runAndWait()