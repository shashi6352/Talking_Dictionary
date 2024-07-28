#GUI Part

from tkinter import *
import json
from difflib import get_close_matches #package to get close match of text
from tkinter import messagebox #package to show message
import pyttsx3 #package to convert text to audio

engine = pyttsx3.init() #creating instance engine class

voice=engine.getProperty("voices")
engine.setProperty("voice",voice[1].id)


####### Function parf
def search():
    data=json.load(open('data.json'))
    word=enterwordEntry.get()
    word=word.lower()
    if word in data:
        meaning=data[word]
        print(meaning)
        textArea.delete(1.0, END)
        for item in meaning:
            textArea.insert(END,U'\u2022'+item+ '\n\n')

    elif len(get_close_matches(word,data.keys())) > 0:
        close_match=get_close_matches(word,data.keys())[0]
        res=messagebox.askyesno('confirm', f'Did you mean {close_match} instead?')
        if res==True:
            enterwordEntry.delete(0,END)
            enterwordEntry.insert(0,close_match)
            meaning=data[close_match]
            textArea.delete(1.0, END)
            for item in meaning:
                textArea.insert(END,U'\u2022'+item+ '\n\n')

        else:
            messagebox.showerror('Error', 'The word doesnt exist, kindly try again')
            enterwordEntry.delete(0, END)
            textArea.delete(1.0, END)


    else:
        messagebox.showinfo('Error','Please enter a valid word!')
        enterwordEntry.delete(0,END)
        textArea.delete(1.0, END)


def clear():
    enterwordEntry.delete(0,END)
    textArea.delete(1.0, END)

def exit():
    res=messagebox.askyesno("Confirm", "Do you want to exit the program?")
    if res == True:
        root.destroy()

    else:
        pass

def wordaudio():
    engine.say(enterwordEntry.get())
    engine.runAndWait()


def meaningaudio():
    engine.say(textArea.get(1.0, END))
    engine.runAndWait()





###########GUI PART

root = Tk()

root.geometry('1000x626+100+50')

root.title('Talking Dictionary created by Shashi Shekhar')

root.resizable(False, False)

#create label to insert background image on screen
bgimage=PhotoImage(file='bg.png')

bgLabel=Label(root,image=bgimage)

bgLabel.place(x=0, y=0)

enterwordLabel=Label(root, text='Enter Word', font=('castellar', 30, 'bold'), fg='red3', bg='whitesmoke')
enterwordLabel.place(x=530, y=20)

enterwordEntry=Entry(root,font=('arial', 20, 'bold'), justify='center', bd=5, relief="groove")
enterwordEntry.place(x=530, y=80)

searchimage=PhotoImage(file='search.png')
searchButton=Button(root, image=searchimage, bg='whitesmoke',bd=0, cursor='hand2', activebackground='whitesmoke', command=search)
searchButton.place(x=580, y=140)

micimage=PhotoImage(file='mic.png')
micButton=Button(root, image=micimage, bg='whitesmoke',bd=0, cursor='hand2', activebackground='whitesmoke', command=wordaudio)
micButton.place(x=700, y=144)

meaningLabel=Label(root, text='Meaning', font=('castellar', 30, 'bold'), fg='red3', bg='whitesmoke')
meaningLabel.place(x=570, y=230)


textArea=Text(root, width=40, height=8, font=('arial', 13, 'bold'), bg='whitesmoke',bd=5, relief="groove")
textArea.place(x=500, y=290)


microphoneimage=PhotoImage(file='microphone.png')
microphoneButton=Button(root, image=microphoneimage, bg='whitesmoke',bd=0, cursor='hand2', activebackground='whitesmoke', command=meaningaudio)
microphoneButton.place(x=540, y=520)


clearimage=PhotoImage(file='clear.png')
clearButton=Button(root, image=clearimage, bg='whitesmoke',bd=0, cursor='hand2', activebackground='whitesmoke', command=clear)
clearButton.place(x=640, y=520)


exitimage=PhotoImage(file='exit.png')
exitButton=Button(root, image=exitimage, bg='whitesmoke',bd=0, cursor='hand2', activebackground='whitesmoke', command=exit)
exitButton.place(x=740, y=520)


def enter_function(event):
    searchButton.invoke()


root.bind('<Return>',enter_function)

root.mainloop()
