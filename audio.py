import PyPDF2
import pyttsx3
from tkinter.filedialog import *

book = askopenfilename()

pdf_reader = PyPDF2.PdfReader(book)

pages = len(pdf_reader.pages)

for num in range(0, pages):
    page = pdf_reader.pages[num]
    text = page.extract_text()
    speak = pyttsx3.init()
    speak.say(text)
    speak.runAndWait()