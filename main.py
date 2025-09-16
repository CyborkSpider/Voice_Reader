import speech_recognition as sr
from tkinter import *
from tkinter.font import Font
import pywinauto
import mishkal.tashkeel

def mn():
    main = Tk()
    main.geometry('800x500')
    main.title("ARTTS")
    main.configure(bg="#000000")
    custom_font = Font(size=25, weight='bold')
    label = Label(main, width=35, padx=40, pady=20, fg="white", bg="black",font=custom_font)
    label.place(x=300, y=150)
    def trans():
        r = sr.Recognizer()
        with sr.Microphone() as src:
            audio = r.listen(src)

        try:
            tash = mishkal.tashkeel.TashkeelClass()
            t = r.recognize_google(audio, language="ar-AR")
            label.config(text=t)
            tash.tashkeel(pywinauto.keyboard.send_keys(str(t)))
        except sr.UnknownValueError as e:
            label.config(text=e)
        except sr.RequestError as f:
            label.config(text=f)
    try:
        trans_btn = Button(main, text="أُكتب", width=6, height=1,
                           padx=0,pady=0, bg="green",fg="white", font=custom_font, command=trans,
                           activebackground='red',activeforeground='yellow')
        trans_btn.place(x=400, y=250)
    except TypeError as g:
        label.config(text=g)
    main.mainloop()
if __name__=="__main__":
    mn()