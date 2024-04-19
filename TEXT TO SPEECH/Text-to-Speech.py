import os
from tkinter import *
from gtts import gTTS
from playsound import playsound

# Get the user's home directory
home_dir = os.path.expanduser("~")

################### Initialized window####################
root = Tk()
root.geometry('350x300')
root.resizable(0,0)
root.config(bg='ghost white')
root.title('MP3SAVED - TEXT_TO_SPEECH')

##heading
Label(root, text='TEXT_TO_SPEECH', font='arial 20 bold', bg='white smoke').pack()
Label(root, text='MP3SAVED', font='arial 15 bold', bg='white smoke').pack(side=BOTTOM)

#label
Label(root, text='Enter Text', font='arial 15 bold', bg='white smoke').place(x=20, y=60)

##text variable
Msg = StringVar()

#Entry
entry_field = Entry(root, textvariable=Msg, width='50')
entry_field.place(x=20, y=100)

###################define function##############################

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text=Message)
    mp3_file_path = os.path.join(home_dir, 'MP3SAVED.mp3')
    speech.save(mp3_file_path)
    playsound(mp3_file_path)

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

#Button
Button(root, text="PLAY", font='arial 15 bold', command=Text_to_speech, width=4).place(x=25, y=140)
Button(root, text='EXIT', font='arial 15 bold', command=Exit, bg='OrangeRed1').place(x=100, y=140)
Button(root, text='RESET', font='arial 15 bold', command=Reset).place(x=175, y=140)

#infinite loop to run program
root.mainloop()
