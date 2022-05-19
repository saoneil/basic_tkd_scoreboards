import tkinter as tk
from datetime import datetime
from pynput import keyboard

window = tk.Tk()
window.minsize(width=720, height=360)

#############################################################################################
########################################TIMER  MODULE########################################

counter = 0
running = False

def counter_label(label):
    def count():
        if running:
            global counter
            tt = datetime.fromtimestamp(counter)
            string = tt.strftime("%M:%S")
            display = string
            label.config(text=display)
            label.after(1000, count)
            counter += 1
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
    global counter
    counter = 0
    if running == False:
        reset['state'] = 'disabled'
        label['text'] = 'Ready'
    else:
        label['text'] = 'Starting...'

time_label = tk.Label(window, text="Ready", fg="black", font="Verdana 150 bold")
time_label.place(relx=0.5, rely=0.12, anchor='center')

start = tk.Button(window, text='Start', width=10, height=2, command=lambda: Start(time_label))
stop = tk.Button(window, text='Stop', width=10, height=2, state='disabled', command=Stop)
reset = tk.Button(window, text='Reset', width=10, height=2, state='disabled', command=lambda: Reset(time_label))
start.place(relx=0.45, rely=0.80, anchor='center')
stop.place(relx=0.55, rely=0.80, anchor='center')
reset.place(relx=0.5, rely=0.95, anchor='center')

#############################################################################################
####################################POINT SCORING SECTION####################################

red_score = 0
blue_score = 0

label_red_score = tk.Label(window, text=red_score, font='Verdana 210 bold', bg='red')
label_blue_score = tk.Label(window, text=blue_score, font='Verdana 210 bold', bg='dodger blue')
label_red_score.place(relx=0.15, rely=0.25, anchor='center')
label_blue_score.place(relx=0.85, rely=0.25, anchor='center')

def single_point_score_red():
    global red_score
    red_score += 1
    label_red_score.config(text=red_score)
def double_point_score_red():
    global red_score
    red_score += 2
    label_red_score.config(text=red_score)
def triple_point_score_red():
    global red_score
    red_score += 3
    label_red_score.config(text=red_score)
def single_point_score_blue():
    global blue_score
    blue_score += 1
    label_blue_score.config(text=blue_score)
def double_point_score_blue():
    global blue_score
    blue_score += 2
    label_blue_score.config(text=blue_score)
def triple_point_score_blue():
    global blue_score
    blue_score += 3
    label_blue_score.config(text=blue_score)

red1point = tk.Button(window, text="1 point", font='Verdana 18 bold', command=single_point_score_red, height=1)
red2point = tk.Button(window, text="2 point", font='Verdana 18 bold', command=double_point_score_red, height=1)
red3point = tk.Button(window, text="3 point", font='Verdana 18 bold', command=triple_point_score_red, height=1)
red1point.place(relx=0.15, rely=0.45, anchor='center')
red2point.place(relx=0.25, rely=0.45, anchor='center')
red3point.place(relx=0.35, rely=0.45, anchor='center')
blue1point = tk.Button(window, text="1 point", font='Verdana 18 bold', command=single_point_score_blue, height=1)
blue2point = tk.Button(window, text="2 point", font='Verdana 18 bold', command=double_point_score_blue, height=1)
blue3point = tk.Button(window, text="3 point", font='Verdana 18 bold', command=triple_point_score_blue, height=1)
blue1point.place(relx=0.65, rely=0.45, anchor='center')
blue2point.place(relx=0.75, rely=0.45, anchor='center')
blue3point.place(relx=0.85, rely=0.45, anchor='center')

#############################################################################################
#######################################WARNING SECTION#######################################

red_warnings = 0
blue_warnings = 0

label_red_warnings = tk.Label(window, text=red_warnings, font='Verdana 75 bold', bg='red')
label_blue_warnings = tk.Label(window, text=blue_warnings, font='Verdana 75 bold', bg='dodger blue')
label_red_warnings.place(relx=0.30, rely=0.62, anchor='center')
label_blue_warnings.place(relx=0.70, rely=0.62, anchor='center')

def red_warning_committed():
    global red_warnings, red_score
    red_warnings += 1
    if divmod(red_warnings, 3)[1] == 0:
        red_score -= 1
    label_red_warnings.config(text=red_warnings)
    label_red_score.config(text=red_score)
def blue_warning_committed():
    global blue_warnings, blue_score
    blue_warnings += 1
    if divmod(blue_warnings, 3)[1] == 0:
        blue_score -= 1
    label_blue_warnings.config(text=blue_warnings)
    label_blue_score.config(text=blue_score)

red1warning = tk.Button(window, text='Warnings', font='Verdana 15 bold', command=red_warning_committed, width=10, height=2)
red1warning.place(relx=0.20, rely=0.62, anchor='center')
blue1warning = tk.Button(window, text='Warnings', font='Verdana 15 bold', command=blue_warning_committed, width=10, height=2)
blue1warning.place(relx=0.80, rely=0.62, anchor='center')

#############################################################################################
########################################FOULS SECTION########################################

red_fouls = 0
blue_fouls = 0

label_red_fouls = tk.Label(window, text=red_fouls, font='Verdana 45 bold', anchor='center', bg='red')
label_blue_fouls = tk.Label(window, text=blue_fouls, font='Verdana 45 bold', anchor='center', bg='dodger blue')
label_red_fouls.place(relx=0.30, rely=0.72, anchor='center')
label_blue_fouls.place(relx=0.70, rely=0.72, anchor='center')

def red_foul_committed():
    global red_fouls, red_score
    red_fouls += 1
    red_score -= 1
    label_red_fouls.config(text=red_fouls)
    label_red_score.config(text=red_score)
def blue_foul_committed():
    global blue_fouls, blue_score
    blue_fouls += 1
    blue_score -= 1
    label_blue_fouls.config(text=blue_fouls)
    label_blue_score.config(text=blue_score)

redfoul = tk.Button(window, text='Fouls', font='Verdana 15 bold', command=red_foul_committed, width=10, height=2)
redfoul.place(relx=0.20, rely=0.72, anchor='center')
bluefoul = tk.Button(window, text='Fouls', font='Verdana 15 bold', command=blue_foul_committed, width=10, height=2)
bluefoul.place(relx=0.80, rely=0.72, anchor='center')

#############################################################################################
######################################POINT/WARNING/FOUL REDUCTION###########################

def red_point_reset():
    global red_score
    red_score = 0
    label_red_score.config(text=red_score)
def blue_point_reset():
    global blue_score
    blue_score = 0
    label_blue_score.config(text=blue_score)
def red_warning_reset():
    global red_warnings
    red_warnings = 0
    label_red_warnings.config(text=red_warnings)
def blue_warning_reset():
    global blue_warnings
    blue_warnings = 0
    label_blue_warnings.config(text=blue_warnings)
def red_foul_reset():
    global red_fouls
    red_fouls = 0
    label_red_fouls.config(text=red_fouls)
def blue_foul_reset():
    global blue_fouls
    blue_fouls = 0
    label_blue_fouls.config(text=blue_fouls)
def reset_all_red():
    global red_score, red_warnings, red_fouls
    red_score, red_warnings, red_fouls = 0,0,0
    label_red_score.config(text=red_score)
    label_red_warnings.config(text=red_warnings)
    label_red_fouls.config(text=red_fouls)
def reset_all_blue():
    global blue_score, blue_warnings, blue_fouls
    blue_score, blue_warnings, blue_fouls = 0,0,0
    label_blue_score.config(text=blue_score)
    label_blue_warnings.config(text=blue_warnings)
    label_blue_fouls.config(text=blue_fouls)


rp_reset = tk.Button(window, text='Reset Red Points', command=red_point_reset, width=15)
bp_reset = tk.Button(window, text='Reset Blue Points', command=blue_point_reset, width=15)
rw_reset = tk.Button(window, text='Reset Red Warning', command=red_warning_reset, width=15)
bw_reset = tk.Button(window, text='Reset Blue Warnings', command=blue_warning_reset, width=15)
rf_reset = tk.Button(window, text='Reset Red Fouls', command=red_foul_reset, width=15)
bf_reset = tk.Button(window, text='Blue Foul Reset', command=blue_foul_reset, width=15)
red_all_reset = tk.Button(window, text='Reset All Red Attr.', command=reset_all_red, width=15)
blue_all_reset = tk.Button(window, text='Reset All Blue Attr.', command=reset_all_blue, width=15)
rp_reset.place(relx=0.83, rely=0.83, anchor='center')
bp_reset.place(relx=0.83, rely=0.88, anchor='center')
rw_reset.place(relx=0.83, rely=0.93, anchor='center')
bw_reset.place(relx=0.83, rely=0.98, anchor='center')
rf_reset.place(relx=0.95, rely=0.83, anchor='center')
bf_reset.place(relx=0.95, rely=0.88, anchor='center')
red_all_reset.place(relx=0.95, rely=0.93, anchor='center')
blue_all_reset.place(relx=0.95, rely=0.98, anchor='center')


COMBINATIONS = []
red = [{keyboard.KeyCode(char='r')}]
blue = [{keyboard.KeyCode(char='b')}]

current = set()

def on_press(key):
    if any([key in COMBO for COMBO in red]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in red):
            single_point_score_red()
    elif any([key in COMBO for COMBO in blue]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in blue):
            single_point_score_blue() 

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)    

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    window.mainloop()
    listener.join()

#window.mainloop()
