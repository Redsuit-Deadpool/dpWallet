from cgitb import text
from tkinter import *
from random import randint
from tkinter.tix import PopupMenu

def passGenerator():

    window = Tk()

    window.title("Password Generator")

    myPassword = chr(randint(33,126))

    def newRand():
        pwEntry.delete(0, END)
        pwLength = int(myEntry.get())

        myPass = ""

        for x in range(pwLength):
            myPass += chr(randint(33, 126))

        pwEntry.insert(0, myPass)

    def clipper():
        window.clipboard_clear()
        window.clipboard_append(pwEntry.get())
        global popUp
        popUp = Toplevel(window)
        popUp.title("Alert ")
        popUp.geometry("150x50")
        popUp.config(bg='systembuttonface')
        alert = Label(popUp,text="Text copied to Clipboard")
        button1 = Button(popUp,text="Ok",command=popUp.destroy)
        alert.pack()
        button1.pack()
    
    lf = LabelFrame(window, text="How many characters?")
    lf.pack(pady=20)
    
    myEntry = Entry(lf, font=("Helvetica", 12))
    myEntry.pack(pady=20, padx=20)
    
    pwEntry = Entry(window, text="", font=("Helvetica", 12), bd=0, bg="systembuttonface")
    pwEntry.pack(pady=20)
    
    myFrame = Frame(window)
    myFrame.pack(pady=20)

    myButton = Button(myFrame, text="Generate Password", command=newRand)
    myButton.grid(row=0, column=0, padx=10)

    clipBtn = Button(myFrame, text="Copy to Clipboard", command=clipper)
    clipBtn.grid(row=0, column=1, padx=10)

    window.mainloop()