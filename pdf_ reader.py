import pyttsx3
import PyPDF2
import os

def pdf_to_speech(pdf_path):
    if not os.path.exists(pdf_path):
        print(f"File '{pdf_path}' not found! Add environment.pdf")
        return
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            print(f"Total Pages: {len(reader.pages)}")
            text = ""
            for i in range(len(reader.pages)):
                t = reader.pages[i].extract_text()
                if t:
                    text += t + " "
            if text:
                print(text[:200])
                engine.say(text)
                engine.runAndWait()
                print("PDF reading done!")
    except Exception as e:
        print(f"Error: {e}")

pdf_to_speech("environment.pdf")
