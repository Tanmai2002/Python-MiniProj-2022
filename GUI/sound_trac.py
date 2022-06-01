# Import the required libraries
from tkinter import *
import pygame
from PIL import Image, ImageTk

# Create an instance of tkinter frame or window
win = Tk()
cur_song=0
# Set the size of the window
# win.geometry("500x300")

# Add a background image
# bg = ImageTk.PhotoImage(file="/Users/muskaansharma/Desktop/Codeshastra2022/icons/microphone.ico")
#
# label = Label(win, image=bg)
# label.place(x=0, y=0)

# Initialize mixer module in pygame
pygame.mixer.init()
options=['Music1', 'Music2', 'Music3']
options_path=['/Users/muskaansharma/Desktop/Codeshastra2022/audio/Calm-and-Peaceful.mp3','/Users/muskaansharma/Desktop/Codeshastra2022/audio/alex-productions-ambient-music-nature.mp3','/Users/muskaansharma/Desktop/Codeshastra2022/audio/Sunset-Landscape.mp3']
clicked = StringVar()
Drop_box = OptionMenu(win, clicked, *options)
Drop_box.pack()
clicked.set("Music1")

# Define a function to play the music
def sound_track():
    global cur_song
    if clicked.get() == "Music1":
        cur_song=0
        pygame.mixer.music.load(options_path[cur_song])
        pygame.mixer.music.play()
    if clicked.get() == "Music2":
        cur_song=1
        pygame.mixer.music.load(options_path[cur_song])
        pygame.mixer.music.play()
    if clicked.get() == "Music3":
        cur_song=2
        pygame.mixer.music.load(options_path[cur_song])
        pygame.mixer.music.play()

# Add a Button widget
b1 = Button(win, text="Play Music", command =sound_track)
b1.pack(pady=60)

win.mainloop()
