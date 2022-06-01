import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import ttk

import cv2
import pandas as pd
import seaborn as sns
import numpy as np
import sys
import pygame
sys.path.append("")
app = Tk()
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)

is_on = True
lv = []
def removeAllTemporary(applet):
    for i in applet.place_slaves()[0:-1]:
        i.place_forget()
        print(i)
    print(applet.place_slaves())
    lv.clear()

app.title('Slumber')
app.geometry('616x411')


# dictionary of colors:
color = {"nero": "#FFFFFF", "#663399": "#663399", "darkorange": "#FE6101"}




# setting switch state:
btnState = False

# loading Navbar icon image:
navIcon = PhotoImage(file="GUI/Menu.png")
closeIcon = PhotoImage(file="GUI/close.png")

  

        
# setting switch function:
def switch():
    global btnState
    if btnState is True:
        # create animated Navbar closing:
        for x in range(301):
            navapp.place(x=-x, y=0)
            topFrame.update()

        # resetting widget colors:
     #    brandLabel.config(bg="gray17", fg="green")
        homeLabel.config(bg=color["#663399"])
        topFrame.config(bg=color["#663399"])
        app.config(bg="white")

        # turning button OFF:
        btnState = False
    else:
        # make app dim:
     #    brandLabel.config(bg=color["nero"], fg="#5F5A33")
        homeLabel.config(bg=color["nero"])
        topFrame.config(bg=color["nero"])
        app.config(bg=color["nero"])

        # created animated Navbar opening:
        for x in range(-300, 0):
            navapp.place(x=x, y=0)
            topFrame.update()

        # turing button ON:
        btnState = True

# top Navigation bar:
topFrame = tk.Frame(app, bg=color["#663399"])
topFrame.pack(side="top", fill=tk.X)

# Header label text:
homeLabel = tk.Label(topFrame, text="Slumber", font="Bahnschrift 15", bg=color["#663399"], height=2, padx=20)
homeLabel.pack(side="right")



#Menu Click
def menuClick():
    removeAllTemporary(app)
    switch()
# Navbar button:
navbarBtn = tk.Button(topFrame, image=navIcon, bg=color["#663399"], activebackground=color["#663399"], bd=0, padx=20, command=menuClick)
navbarBtn.place(x=10, y=10)

# setting Navbar frame:
navapp = tk.Frame(app, bg="white", height=1000, width=200)
navapp.place(x=-300, y=0)
tk.Label(navapp, font="Bahnschrift 15", bg=color["#663399"], fg="white", height=2, width=300, padx=20).place(x=0, y=0)

# set y-coordinate of Navbar widgets:
y = 80
################################################################
def db_click():
    global img
    # messagebox.showinfo("Dashboard Popup")
    removeAllTemporary(app)
    switch()
    dashBoardLabel = Label(app,text="Today's Activity",bg="white",font = ('bold 15 underline')).place(x=240,y=60)
    lv.append(dashBoardLabel)
    init_figure = create_figure()
    canvas = FigureCanvasTkAgg(init_figure, master=app)
    canvas.draw()
    canvas.get_tk_widget().place(x=100,y=150)
    from PIL import Image,ImageTk
    img=cv2.imread('./temp.png')
    scale_percent = 40  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    img = ImageTk.PhotoImage(image=Image.fromarray(resized))
    label=tk.Label(app,image=img)
    label.place(x=300,y=150)
# ##############################################
def create_figure() -> Figure:
    # generate some data
    matrix = np.random.randint(20, size=(10, 10))
    # plot the data
    figure = Figure(figsize=(2, 2))
    ax = figure.subplots()
    df=pd.read_csv('./logs.csv')
    sns.countplot(x="Position", data=df,ax=ax)
    # sns.heatmap(matrix, square=True, cbar=False, ax=ax)
    return figure


# list of squares
#     y = [i**2 for i in range(101)]
#
# # adding the subplot
#     plot1 = fig.add_subplot(111)
#
# # plotting the graph
#     plot1.plot(y)

    # creating the Tkinter canvas# containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
							master = app)
    canvas.draw()
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().place(x=50,y=50)

def SA_click():
    
    # messagebox.showinfo("Sleep Analytics Popup")
    switch()
    removeAllTemporary(app)
    app.resizable(width = 1, height = 1)
    
    # Using treeview widget
    treev = ttk.Treeview(app, selectmode ='browse')
    import pandas as pd
    df=pd.read_csv('Daily_logs.csv')
    df.dropna(inplace=True)
    # Calling pack method w.r.to treeview
    treev.place(x=90,y=80)
    
    # Constructing vertical scrollbar
    # with treeview
    verscrlbar = ttk.Scrollbar(app,
                               orient ="vertical",
                               command = treev.yview)
    
   
    
    # Defining number of columns
    treev["columns"] = ("1", "2", "3")
    
    # Defining heading
    treev['show'] = 'headings'
    
    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", width = 80, anchor ='c')
    treev.column("2", width = 80, anchor ='c')
    treev.column("3", width = 80, anchor ='c')

   
    # respective columns
    treev.heading("1", text ="Date")
    treev.heading("2", text ="Time of Sleep")
    treev.heading("3", text ="Perfect sleep(%)")
    cols = list(df.columns)
    treev["columns"] = cols
    for i in cols:
        treev.column(i,  width = 120,anchor="c")
        treev.heading(i, text=i, anchor='c')

    for index, row in df.iterrows():
        treev.insert("",0,text=index,values=list(row))

   
def Track_click():
    switch()
    removeAllTemporary(app)

    # import sleep_tracker
    trackBtn = tk.Button(app,text="Start Tracking", font="BahnschriftLight 15",fg='black',bg="#663399",bd=0,activebackground="green",activeforeground="white").place(x=20, y=120)
    # dashBoardLabel.destroy()
    minutes=0
    att = tk.Frame(app,bg='white',highlightbackground= "#663399",highlightcolor= "#663399",highlightthickness=2,height=300,width=350).place(x=200,y=80)
    playListLabel = tk.Label(att, text = "Sleep Playlist",bg='white',font = 'bold 14 underline').place(x=220,y=100)
    playListLabel = tk.Label(att, text = "Set Alarm",bg='white',font = 'bold 14 underline').place(x=220,y=220)
    def off():
        toggle_photo.configure(file='off.png')
        toggle_button.configure(command=on)
        # onoff.configure(text='Off')
    def on():
        toggle_photo.configure(file='on.png')
        toggle_button.configure(command=off)
        # onoff.configure(text='On')


    toggle_photo = PhotoImage(file='on.png')
    toggle_button = Button(att,image=toggle_photo,border=0,command=off)
    toggle_button.place(x=400,y=260)

    pygame.mixer.init()
    options = ['Music1', 'Music2', 'Music3','None']
    options_path = ['./GUI/Calm-and-Peaceful.mp3',
                    './GUI/alex-productions-ambient-music-nature.mp3',
                    './GUI/Sunset-Landscape.mp3','']
    clicked = StringVar()
    Drop_box = OptionMenu(att, clicked, *options)
    Drop_box.place(x=220,y=130)
    clicked.set("Music1")


    def sound_track():
        global cur_song
        if clicked.get() == "Music1":
            cur_song = 0
            pygame.mixer.music.load(options_path[cur_song])
            pygame.mixer.music.play()
        if clicked.get() == "Music2":
            cur_song = 1
            pygame.mixer.music.load(options_path[cur_song])
            pygame.mixer.music.play()
        if clicked.get() == "Music3":
            cur_song = 2
            pygame.mixer.music.load(options_path[cur_song])
            pygame.mixer.music.play()
        if clicked.get()=='None':
            pygame.mixer.music.stop()
        import sleep_tracker
        sleep_tracker.start_tracking()

    hour= StringVar()
    hourBox=OptionMenu(att,hour,*[str(i) for i in range(24)])
    hourBox.place(x=220,y=255)
    min = StringVar()
    minBox = OptionMenu(att, min, *[str(i) for i in range(60)])
    minBox.place(x=280, y=255)
    def stop_fun():
        pygame.mixer.music.stop()
        cv2.destroyAllWindows()
    trackBtn = tk.Button(app, text="Start Tracking", font="BahnschriftLight 15", fg='black', bg="#663399", bd=0, activebackground="green", activeforeground="white",command=sound_track).place(x=20, y=120)
    StopBtn = tk.Button(app, text="Stop Tracking", font="BahnschriftLight 15", fg='black', bg="#663399", bd=0,activebackground="green", activeforeground="white",command=stop_fun).place(x=20, y=180)



    
DashboardBtn = tk.Button(navapp,text = "Today's Activity", font="BahnschriftLight 15 underline", bg="white", fg=color["#663399"], activeforeground="green", bd=0,command = db_click).place(x=25, y=y)
y += 60
ActivityBtn = tk.Button(navapp,text = "Sleep Analytics", font="BahnschriftLight 15 underline", bg="white", fg=color["#663399"], activeforeground="green", bd=0,command = SA_click).place(x=25, y=y)
y += 60
TrackBtn = tk.Button(navapp,text = "Tracking", font="BahnschriftLight 15 underline", bg="white", fg=color["#663399"], activeforeground="green", bd=0,command = Track_click).place(x=25, y=y)
y += 60
# ActivityBtn = tk.Button(navapp,text = "Tracking", font="BahnschriftLight 15 underline", bg="white", fg=color["purple"], activeforeground="green", bd=0,command = db_click).place(x=25, y=y)
# y += 60
# Track_click()

# Navbar Close Button:
closeBtn = tk.Button(navapp,image=closeIcon, bg=color["#663399"], activebackground=color["#663399"], bd=0, command=switch)
closeBtn.place(x=150, y=10)

# window in mainloop:

app.mainloop()

