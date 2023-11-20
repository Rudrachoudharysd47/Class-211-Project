import socket
from tkinter import *
import tkinter as tk
from playsound import playsound
import pygame
from pygame import mixer
import ftplib
from ftplib import FTP
import os
import time
import ntpath
from pathlib import Path


PORT  = 8050
IP_ADDRESS = "127.0.0.1"
SERVER = None
BUFFER_SIZE = 4096

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    musicWindow()
setup()


def play():
    global song_selected
    song_selected = listbox.get(ANCHOR)

    pygame 
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()
    if(song_selected !=""):
        infoLabel.configure(text = "Now Playing: "+ song_selected)
    else:
        infoLabel.configure(text = "")

def stop():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shred_files/'+song_selected)
    mixer.music.pause()
    infoLabel.congigure(text = "")

def resume():
    global song_selected
    mixer.init()
    mixer.music.load('shred_files/'+song_selected)
    mixer.music.play()

def pause():
    global song_selected
    pygame

    mixer.init()
    mixer.music.load('shred_files/'+song_selected)
    mixer.music.pause()

def browseFiles():
    global Listbox
    global song_counter
    global filePathLabel

    try:
        filename = filedialog.askopenfilename()
        HOSTNAME = "127.0.0.1"
        USERNAME = "lftpd"
        PASSWORD = "lftpd"

        ftp_server = FTP(HOSTNAME, USERNAME, PASSWORD)
        ftp_server.encoding = "utf-8"
        ftp_server.cwd('shared_files')
        fname = ntpath.basename(filename)
        with open(filename, 'rb')as file:
            ftp_server.storybinary(f"STOR{fname}", file)

        ftp_server.dir()
        ftp_server.quit()

    except FileNotFoundError:
        print("Cancel Button Pressed")


def musicWindow():
    window = Tk()
    window.title('Music Window')
    window.geometry("300x300")
    window.configure(bg = 'LightSkyBlue')


    selectLabel = Label(window, text = "Select Song", bg = "LightSkyBlue", font = ("Calibri", 8))
    selectLabel.place(x = 2,  y = 1)

    listbox = Listbox(window , height = 10, width = 39, sctivestyle = 'dotbox', bg = 'LightSkyBlue', borderwidth = 2 , font = ("Calibri" , 10))
    listbox.place(x = 10 , y = 10 )

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)
 
    playButton = Button(window , text = "play" , width = 10, bd = 1 , bg = 'SkyBlue' , font = ("Calibri",10), command = play)
    playButton.place(x = 30, y = 200)

    stop= Button(window, text = "Stop", bd  =1, width = 10 , bg = "SkyBlue", font = ("Calibri", 10) , command = stop)
    stop.place(x = 200 , y = 200)

    upload= Button(window, text = "Upload", bd  =1, width = 10 , bg = "SkyBlue", font = ("Calibri", 10))
    upload.place(x = 30 , y = 250)

    Download = Button(window, text = "Download", bd  =1, width = 10 , bg = "SkyBlue", font = ("Calibri", 10))
    Download.place(x = 200 , y = 250)

    infoLabel= Button(window, text = "", fg = "blue", font = ("Calibri", 10))
    infoLabel.place(x = 200 , y = 200)

    ResumeButton = Button(window , text = 'Resume', width = 10, bd = 1 , bg = 'SkyBlue' , font = ('Calibri',10) , command = resume)
    ResumeButton.place(x = 30, y = 250)

    PauseButton = Button(window, text = "Pause", width = 10, bd = 1, bg= "SkyBlue" , font = ("Calbri",10), command=pause)
    PauseButton.place(x = 200 , y = 250)

    window.mainloop()