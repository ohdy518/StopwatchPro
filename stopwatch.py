print("Copyright 2021. codingPro01. All Rights Reserved. ")
print("Booting up...")
import tkinter as tk
import time, datetime
from win32api import GetSystemMetrics, SetClassLong
root = tk.Tk()
run = False
f = True
psec = 0
sec = 0
_fullscreen = False
def time_synt(time=float):
    spl_str_time = str(time).split(".")
    time_sec = int(spl_str_time[0])
    time_ms = int(spl_str_time[1])
    min = 0
    hour = 0
    for i in "*" * (time_sec // 60):
        min += 1
        time_sec -= 60
    for i in "*" * (min // 60): 
        hour += 1
        min -= 60
    if len(str(time_ms)) < 3:
        time_ms = ("0" * (3 - len(str(time_ms)))) + str(time_ms) 
    if len(str(time_sec)) < 2:
        time_sec = ("0" * (2 - len(str(time_sec)))) + str(time_sec)
    if len(str(min)) < 2:
        min = ("0" * (2 - len(str(min)))) + str(min)
    if len(str(hour)) < 2:
        hour = str(hour) + ("0" * (2 - len(str(hour))))
    mix = f"{hour}:{min}:{time_sec}.{time_ms}"
    return mix
def quit(_):
    root.destroy()
def fstart():
    global run, f, psec
    f = False
    run = True
    old_time = time.time()
    while run:
        global psec
        root.update()
        nowtime = time.time()
        psec = nowtime - old_time
        stopwatch.config(text=time_synt(round(psec, 3)), fg="#00ff00")
    stopwatch.config(fg="#ff0000")
def start():
    global run, sec
    run = True
    old_time = time.time()
    while run:
        global sec
        root.update()
        nowtime = time.time()
        sec = (nowtime - old_time) + psec
        stopwatch.config(text=time_synt(round(sec, 3)), fg="#00ff00")
    stopwatch.config(fg="#ff0000")
def stop():
    global run
    run = False
    stopwatch.config(fg="#ff0000")
    root.update()
def reset(_):
    global sec, psec
    sec = 0.000
    psec = 0.000
    stopwatch.config(text="00:00:00.000", fg="#fcba03")
pressed_data = False
def press(_):
    global pressed_data, psec
    if pressed_data:
        pressed_data = False
        stop()
    else:
        pressed_data = True
        if f:
            
            fstart()
        else:
            start()
            psec = sec
def fullscreen(_=None):
    global _fullscreen
    _fullscreen = True
    root.attributes("-fullscreen", True)
    stopwatch.config(font=("Arial", 144))
    stopwatch.place(height=200)
def unfullscreen(_=None):
    global _fullscreen
    _fullscreen = False
    root.attributes("-fullscreen", False)
    root.geometry("200x40")
    stopwatch.config(font=("Arial", 24))
    stopwatch.pack()
def fullscreen_unfullscreen(_=None):
    if _fullscreen == True:
        unfullscreen()
    else:
        fullscreen()
root.title("Stopwatch")
root.iconbitmap("app.ico")
root.attributes("-fullscreen", False)
root.attributes("-topmost", True)
root.geometry("200x40")
root.update()
root.bind("<Escape>", quit)
root.bind("<q>", quit)
root.bind("<space>", press)
root.bind("<r>", reset)
root.bind("<f>", fullscreen_unfullscreen)
stopwatch = tk.Label(text="00:00:00.000", fg="#fcba03")

stopwatch.config(font=("Arial", 24))
stopwatch.pack()
time.sleep(1)
print("Ready!")
root.mainloop()