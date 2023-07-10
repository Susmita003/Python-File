import pygame
from logging import config
from tkinter import *
import fnmatch
import os
from pygame import mixer 

mixer.init()

Canvas = Tk()
Canvas.title("** Susmita Own Music Player **")    # music player name
Canvas.geometry("600x500+220+20")                 # music player diemantion
Canvas.config(bg="khaki1")                        # music player background

# for Music Player 

listBox=Listbox(Canvas, fg="dark green", bg="green yellow", width="1000",height="10",font=("Times New Roman",12,"bold"))   
listBox.pack(padx=15, pady=10)


rootpath= "C:\\Users\mukhe\OneDrive\Desktop\Music Folder"   #music list path
pattern="*.mp3"

listBox.insert(0,"Songs....\n")
listBox.insert(1,"\n")

for root,dirs,files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        listBox.insert("end",filename)


# for buttons file image path

prev_image=PhotoImage(file="D:\\Python Programs\\programs\\Python project\\prev_img.png")
stop_image=PhotoImage(file="D:\\Python Programs\\programs\\Python project\\stop_img.png")
play_image=PhotoImage(file="D:\\Python Programs\\programs\\Python project\\play_img.png")
pause_image=PhotoImage(file="D:\\Python Programs\\programs\\Python project\\pause_img.png")
next_image=PhotoImage(file="D:\\Python Programs\\programs\\Python project\\next_img.png")

# function for play music

def select():
    label.config(text=listBox.get("anchor"))
    mixer.music.load(rootpath+"\\"+listBox.get("anchor"))
    mixer.music.play()

# function for stop music

def stop():
    mixer.music.stop()
    listBox.select_clear("active")

# function for play next music

def  play_next():
    next_song=listBox.curselection()
    next_song=(next_song[0]+1)
    next_song_name=listBox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(rootpath+"\\"+next_song_name)
    mixer.music.play()

    listBox.select_clear(0,"end")
    listBox.activate(next_song)
    listBox.select_set(next_song)

#  function for play previous music

def  play_prev():
    prev_song=listBox.curselection()
    prev_song=(prev_song[0]-1)
    prev_song_name=listBox.get(prev_song)
    label.config(text=prev_song_name)

    mixer.music.load(rootpath+"\\"+prev_song_name)
    mixer.music.play()

    listBox.select_clear(0,"end")
    listBox.activate(prev_song)
    listBox.select_set(prev_song)

# function for pause music

def pause_song():
    if pauseButton["text"]=="Pause":
        mixer.music.pause()
        pauseButton["text"]="Play"
    else:
        mixer.music.unpause()
        pauseButton["text"]="Pause"

    
# which song play at the moments that backgraound

label=Label(Canvas,text="",fg="Black", bg="khaki1",font=("Times New Roman",15,"bold"))
label.pack(pady=10)

# for button backgraound

top=Frame(Canvas,bg="khaki1")
top.pack(anchor="center")

# for show the buttons

prevButton=Button(Canvas,text="Prev", image=prev_image,fg="black",bg="khaki1",borderwidth=0, command=play_prev)
prevButton.pack(pady=10, in_=top, side="left")


stopButton=Button(Canvas,text="Stop",image=stop_image,fg="black",bg="khaki1",borderwidth=0, command=stop)
stopButton.pack(pady=10, in_=top, side="left")


playButton=Button(Canvas,text="Play",image=play_image,fg="black",bg="khaki1",borderwidth=0, command=select)
playButton.pack(pady=10, in_=top, side="left")


pauseButton=Button(Canvas,text="Pause",image=pause_image,fg="black",bg="khaki1",borderwidth=0, command=pause_song)
pauseButton.pack(pady=10, in_=top, side="left")


nextButton=Button(Canvas,text="Next",image=next_image,fg="black",bg="khaki1",borderwidth=0, command=play_next)
nextButton.pack(pady=10, in_=top, side="left")


Canvas.mainloop()