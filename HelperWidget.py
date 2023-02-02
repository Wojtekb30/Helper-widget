app_id = "KEY-HERE" #wolfram key here
import wolframalpha
global e1 #import everything, make the input/text boxes global
global e2
client = wolframalpha.Client(app_id)
from googletrans import Translator
translator = Translator()
import tkinter as tk
root = tk.Tk() #start TKinter and set window attributes:
root.title("Helper widget")
root.geometry('486x200')
root.attributes('-topmost', True) #window always on top (comment or delete this line to disable always on top)
root.resizable(0,0)

def wolf(): #wolfram api function
    global e2
    global e1
    tekst = str(e1.get()) #get question
    res = client.query(tekst) #sent to Wolfram
    answer = str(next(res.results).text) #get answer text
    #render the answer window again and with the answer:
    e2.destroy()
    e2 = tk.Text(root, width=60, height=1000)
    e2.insert("end-1c",answer)
    e2.grid(row=3)
    
def tlumacz(): #translator funtion
    global e1
    global e2
    lang = str(e1.get()).split("-") #get languages
    tekst = str(e2.get("1.0",'end-1c')) #get text to translate
    tlumacz = translator.translate(tekst, dest=str(lang[1]), src=str(lang[0])) #translate
    tempwynik = str(tlumacz.text) #get result
    #render the answer window again and with the translation:
    e2.destroy()
    e2 = tk.Text(root, width=60, height=100)
    e2.insert("end-1c",tempwynik)
    e2.grid(row=3)
    
#render the window:
e1 = tk.Entry(root, width=60)
e1.grid(row=0)
btnwolf = tk.Button(root, text="Send to Wolfram", command=wolf)
btntranslate = tk.Button(root, text="Translate", command=tlumacz)
btnwolf.grid(row=1, column=0)
btntranslate.grid(row=2, column=0)
e2 = tk.Text(root, width=60, height=100)
e2.insert("end-1c","To translate, type text to translate into this box and in   the top box write [source language]-[destination language]  (for example en-pl)")
e2.grid(row=3)

root.mainloop()
