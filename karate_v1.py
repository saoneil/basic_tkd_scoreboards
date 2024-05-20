import tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import datetime
from pynput import keyboard
import pygame
import time, os
from pathlib import Path

def quit_me():
    print('quit')
    root.quit()
    root.destroy()
    quit()

root = tk.Tk()
root.title("PMA | Class Sparring")
root.protocol("WM_DELETE_WINDOW", quit_me)
root.geometry('1000x500')

canv = Canvas(root, bg="white", height=1000, width=500)
img_filename3 = PhotoImage(file=r'C:\\Users\\saone\\Documents\\Python Stuff\\basic_tkd_scoreboards\\bg_image - kumite.png')
background_label3 = Label(root, image=img_filename3)
background_label3.place(x=0, y=0, relwidth=1, relheight=1)
canv.pack()

counter = 0
running = False
red_score = 0
red_warnings_count = 0
senshu_aka = 0
blue_score = 0
blue_warnings_count = 0
senshu_ao = 0


pygame.mixer.init()

def play_sound(sound_type):
    root_dir = Path(__file__).resolve().parent
    if sound_type == "short_beep":
        pygame.mixer.music.load(root_dir / "short_beep.mp3")
        pygame.mixer.music.play()
    elif sound_type == "long_beep":
        pygame.mixer.music.load(root_dir / "long_beep.mp3")
        pygame.mixer.music.play()
def update_counter(*args):
    selected_time = time_var.get()
    time_label.config(text=str(selected_time))
    hours, minutes = map(int, selected_time.split(':'))
    global counter
    counter = hours * 60 + minutes
def counter_label(label):
    def count():
        global counter
        if running:
            tt = datetime.fromtimestamp(counter)
            string = tt.strftime("%M:%S")
            print(string)
            display = string
            label.config(text=display)
            label.after(1000, count)
            counter -= 1
            if counter == 14:
                play_sound("short_beep")
                time.sleep(0.3)
                play_sound("short_beep")
            if counter == -1:
                Stop()
                play_sound("long_beep")
    count()
def Start(label):
    global running
    running = True
    counter_label(label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'
def Stop():
    global running
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    running = False
def Reset(label):
    update_counter()
    if running == False:
        reset['state'] = 'disabled'
        label['text'] = time_var.get()
    else:
        label['text'] = 'Starting...'
def single_point_score_red():
    global red_score
    red_score += 1
    label_red_score.config(text=red_score)
def remove_single_point_red():
    global red_score
    red_score -= 1
    label_red_score.config(text=red_score)
def single_point_score_blue():
    global blue_score
    blue_score += 1
    label_blue_score.config(text=blue_score)
def remove_single_point_blue():
    global blue_score
    blue_score -= 1
    label_blue_score.config(text=blue_score)
def reset_all():
    global red_score, red_warnings_count
    global blue_score, blue_warnings_count
    global senshu_aka, senshu_ao
    red_score, red_warnings_count = 0, 0
    blue_score, blue_warnings_count = 0, 0
    senshu_aka, senshu_ao = 0, 0
    label_red_score.config(text=red_score)
    label_red_chui.config(text=red_warnings_count*"* ")
    label_red_senshu.config(text=senshu_aka*"⧆")
    label_blue_score.config(text=blue_score)
    label_blue_chui.config(text=blue_warnings_count*"* ")
    label_blue_senshu.config(text=senshu_ao*"⧆")
def warn_red():
    global red_warnings_count
    red_warnings_count += 1
    label_red_chui.config(text=red_warnings_count*"* ")
def remove_red_warn():
    global red_warnings_count
    red_warnings_count -= 1
    label_red_chui.config(text=red_warnings_count*"* ")
def warn_blue():
    global blue_warnings_count
    blue_warnings_count += 1
    label_blue_chui.config(text=blue_warnings_count*"* ")
def remove_blue_warn():
    global blue_warnings_count
    blue_warnings_count -= 1
    label_blue_chui.config(text=blue_warnings_count*"* ")
def award_seshu_aka():
    global senshu_aka
    senshu_aka = (senshu_aka + 1) % 2
    label_red_senshu.config(text=senshu_aka*"⧆")
def award_senshu_ao():
    global senshu_ao
    senshu_ao = (senshu_ao + 1) % 2
    label_blue_senshu.config(text=senshu_ao*"⧆")

time_var = tk.StringVar(root)
time_var.set("Select Timer")
option_list = ["02:00", "02:30", "03:00", "01:00", "00:30", "00:18", "00:25"]
timer_select = tk.OptionMenu(root, time_var, *option_list)
timer_select.place(relx=0.5, rely=0.45, anchor="center")
counter = tk.IntVar(root)
time_var.trace('w', update_counter)

time_label = tk.Label(root, text="00:00", fg="white", font="Verdana 100 bold", bg="black", width=50)
time_label.place(relx=0.5, rely=0.55, anchor='center')

start = tk.Button(root, text='Start', font="Verdana 10 bold", command=lambda: Start(time_label))
start.place(relx=0.5, rely=0.89, anchor='center')
stop = tk.Button(root, text='Stop', font="Verdana 10 bold", state='disabled', command=Stop)
stop.place(relx=0.5, rely=0.92, anchor='center')
reset = tk.Button(root, text='Reset', font="Verdana 10 bold", state='disabled', command=lambda: Reset(time_label))
reset.place(relx=0.5, rely=0.95, anchor='center')
reset_all = tk.Button(root, text='Reset Scores', font='verdana 10 bold', command=reset_all)
reset_all.place(relx=0.5, rely=0.98, anchor='center')

label_red_score = tk.Label(root, text=red_score, font='Verdana 300 bold', bg='#ed1c24', fg='yellow')
label_red_score.place(relx=0.25, rely=0.00, anchor='n')
senshu_aka_button = tk.Button(root, text="AKA", font="verdana 35 bold", command=award_seshu_aka)
senshu_aka_button.place(relx=0.25, rely=0.05, anchor='center')
button_red_warn = tk.Button(root, text="Penalty:", font="verdana 25 bold", command=warn_red)
button_red_warn.place(relx=0.05, rely=0.67, anchor='w')
label_red_chui = tk.Label(root, text=red_warnings_count*"* ", font="verdana 100 bold", bg='#ed1c24', fg='yellow')
label_red_chui.place(relx=0.05, rely=0.8, anchor='w')
label_red_senshu = tk.Label(root, text=senshu_aka*"⧆", fg="yellow", font="versana 50 bold", bg="#ed1c24")
label_red_senshu.place(relx=0.40, rely=0.12, anchor='w')

label_blue_score = tk.Label(root, text=blue_score, font='Verdana 300 bold', bg='#2744a0', fg='yellow')
label_blue_score.place(relx=0.75, rely=0.00, anchor='n')
senshu_ao_button = tk.Button(root, text="AO", font="verdana 35 bold", command=award_senshu_ao)
senshu_ao_button.place(relx=0.75, rely=0.05, anchor='center')
button_blue_warn = tk.Button(root, text="Penalty:", font="verdana 25 bold", command=warn_blue)
button_blue_warn.place(relx=0.55, rely=0.67, anchor='w')
label_blue_chui = tk.Label(root, text=blue_warnings_count*"* ", font="verdana 100 bold", bg='#2744a0', fg='yellow')
label_blue_chui.place(relx=0.55, rely=0.8, anchor='w')
label_blue_senshu = tk.Label(root, text=senshu_ao*"⧆", fg="yellow", font="versana 50 bold", bg="#2744a0")
label_blue_senshu.place(relx=0.90, rely=0.12, anchor='w')

red_dec_score = tk.Button(root, text="-", font="verdana 10 bold", command=remove_single_point_red)
red_dec_score.place(relx=0.207, rely=0.07)
red_inc_score = tk.Button(root, text="+", font="verdana 10 bold", command=single_point_score_red)
red_inc_score.place(relx=0.279, rely=0.07)
blue_dec_score = tk.Button(root, text="-", font="verdana 10 bold", command=remove_single_point_blue)
blue_dec_score.place(relx=0.716, rely=0.07)
blue_inc_score = tk.Button(root, text="+", font="verdana 10 bold", command=single_point_score_blue)
blue_inc_score.place(relx=0.77, rely=0.07)

red_dec_warn = tk.Button(root, text="-", font="verdana 10 bold", command=remove_red_warn)
red_dec_warn.place(relx=0.05, rely=0.68)
blue_dec_warn = tk.Button(root, text="-", font="verdana 10 bold", command=remove_blue_warn)
blue_dec_warn.place(relx=0.55, rely=0.68)



# COMBINATIONS = []
# red = [{keyboard.KeyCode(char='r')}]
# blue = [{keyboard.KeyCode(char='b')}]
# timestart = [{keyboard.KeyCode(char='q')}]
# timepause = [{keyboard.KeyCode(char='p')}]
# timerestart = [{keyboard.KeyCode(char='l')}]
# current = set()

# def on_press(key):
#     if any([key in COMBO for COMBO in red]):
#         current.add(key)
#         if any(all(k in current for k in COMBO) for COMBO in red):
#             single_point_score_red()
#     elif any([key in COMBO for COMBO in blue]):
#         current.add(key)
#         if any(all(k in current for k in COMBO) for COMBO in blue):
#             single_point_score_blue()
#     elif any([key in COMBO for COMBO in timestart]):
#         current.add(key)
#         if any(all(k in current for k in COMBO) for COMBO in timestart):
#             Start(time_label)
#     elif any([key in COMBO for COMBO in timepause]):
#         current.add(key)
#         if any(all(k in current for k in COMBO) for COMBO in timepause):
#             Stop()
#     elif any([key in COMBO for COMBO in timerestart]):
#         current.add(key)
#         if any(all(k in current for k in COMBO) for COMBO in timerestart):
#             Reset(time_label)
# def on_release(key):
#     if any([key in COMBO for COMBO in COMBINATIONS]):
#         current.remove(key)    
# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#     root.mainloop()
#     listener.join()


root.mainloop()