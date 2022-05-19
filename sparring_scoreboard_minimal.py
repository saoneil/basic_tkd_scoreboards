import tkinter as tk
from datetime import datetime
from pynput import keyboard

def quit_me():
    print('quit')
    root.quit()
    root.destroy()
    quit()

root = tk.Tk()
root.title("Performance Taekwon-Do | Simple Scoring App")
root.protocol("WM_DELETE_WINDOW", quit_me)

root.grid_columnconfigure(1,weight=1)
root.grid_columnconfigure(2,weight=1)
root.grid_columnconfigure(3,weight=1)
root.grid_columnconfigure(4,weight=1)
root.grid_columnconfigure(5,weight=1)
root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(1,weight=1)
root.grid_rowconfigure(2,weight=1)
root.grid_rowconfigure(3,weight=1)
root.grid_rowconfigure(4,weight=1)
root.grid_rowconfigure(5,weight=1)
root.grid_rowconfigure(6,weight=1)
root.grid_rowconfigure(7,weight=1)
root.grid_rowconfigure(8,weight=1)

counter = 0
running = False
red_score = 0
blue_score = 0
red_warnings = 0
blue_warnings = 0
red_fouls = 0
blue_fouls = 0

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
def reset_all():
    global red_score, red_warnings, red_fouls
    global blue_score, blue_warnings, blue_fouls
    red_score, red_warnings, red_fouls = 0,0,0
    blue_score, blue_warnings, blue_fouls = 0,0,0
    label_red_score.config(text=red_score)
    label_blue_score.config(text=blue_score)
    label_red_warnings.config(text=red_warnings)
    label_blue_warnings.config(text=blue_warnings)
    label_red_fouls.config(text=red_fouls)
    label_blue_fouls.config(text=blue_fouls)

time_label = tk.Label(root, text="Ready", fg="black", font="Verdana 120 bold")
time_label.grid(row=1, column=3)
start = tk.Button(root, text='Start', font="Verdana 20 bold", width=10, height=2, command=lambda: Start(time_label))
stop = tk.Button(root, text='Stop', font="Verdana 20 bold", width=10, height=2, state='disabled', command=Stop)
reset = tk.Button(root, text='Reset', font="Verdana 20 bold", width=10, height=2, state='disabled', command=lambda: Reset(time_label))
start.grid(row=2, column=3)
stop.grid(row=3, column=3)
reset.grid(row=7, column=3)

label_red_score = tk.Label(root, text=red_score, font='Verdana 225 bold', bg='red')
label_blue_score = tk.Label(root, text=blue_score, font='Verdana 225 bold', bg='dodger blue')
label_red_warnings = tk.Label(root, text=red_warnings, font='Verdana 100 bold', bg='red')
label_blue_warnings = tk.Label(root, text=blue_warnings, font='Verdana 100 bold', bg='dodger blue')
# red1point = tk.Button(root, text="1 point", font='Verdana 15 bold', command=single_point_score_red, width = 6, height=1)
# red2point = tk.Button(root, text="2 point", font='Verdana 15 bold', command=double_point_score_red, width = 6, height=1)
# red3point = tk.Button(root, text="3 point", font='Verdana 15 bold', command=triple_point_score_red, width = 6, height=1)
# blue1point = tk.Button(root, text="1 point", font='Verdana 15 bold', command=single_point_score_blue, width = 6, height=1)
# blue2point = tk.Button(root, text="2 point", font='Verdana 15 bold', command=double_point_score_blue, width = 6, height=1)
# blue3point = tk.Button(root, text="3 point", font='Verdana 15 bold', command=triple_point_score_blue, width = 6, height=1)
# red1warning = tk.Button(root, text='Warn', font='Verdana 15 bold', command=red_warning_committed, width = 6, height=1)
# blue1warning = tk.Button(root, text='Warn', font='Verdana 15 bold', command=blue_warning_committed, width = 6, height=1)
label_red_fouls = tk.Label(root, text=red_fouls, font='Verdana 55 bold', anchor='center', bg='red')
label_blue_fouls = tk.Label(root, text=blue_fouls, font='Verdana 55 bold', anchor='center', bg='dodger blue')
redfoul = tk.Button(root, text='Fouls', font='Verdana 15 bold', command=red_foul_committed, width=6, height=1)
bluefoul = tk.Button(root, text='Fouls', font='Verdana 15 bold', command=blue_foul_committed, width=6, height=1)
reset_all = tk.Button(root, text='Reset Scores', command=reset_all, width=15)


label_red_score.grid(row=1, column=1)
label_red_warnings.grid(row=2, column=1)
label_red_fouls.grid(row=3, column=1)
# red1point.grid(row=4, column=2)
# red2point.grid(row=5, column=2)
# red3point.grid(row=6, column=2)
# red1warning.grid(row=7, column=2)
# redfoul.grid(row=8, column=2)

label_blue_score.grid(row=1, column=5)
label_blue_warnings.grid(row=2, column=5)
label_blue_fouls.grid(row=3, column=5)
# blue1point.grid(row=4, column=4)
# blue2point.grid(row=5, column=4)
# blue3point.grid(row=6, column=4)
# blue1warning.grid(row=7, column=4)
# bluefoul.grid(row=8, column=4)

reset_all.grid(row=8, column=3)


COMBINATIONS = []
red = [{keyboard.KeyCode(char='r')}]
blue = [{keyboard.KeyCode(char='b')}]
redwarn = [{keyboard.KeyCode(char='t')}]
bluewarn = [{keyboard.KeyCode(char='n')}]
redfoul = [{keyboard.KeyCode(char='y')}]
bluefoul = [{keyboard.KeyCode(char='m')}]
timestart = [{keyboard.KeyCode(char='q')}]
timepause = [{keyboard.KeyCode(char='a')}]
timerestart = [{keyboard.KeyCode(char='z')}]
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
    elif any([key in COMBO for COMBO in redwarn]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in redwarn):
            red_warning_committed()
    elif any([key in COMBO for COMBO in bluewarn]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in bluewarn):
            blue_warning_committed()
    elif any([key in COMBO for COMBO in redfoul]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in redfoul):
            red_foul_committed()
    elif any([key in COMBO for COMBO in bluefoul]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in bluefoul):
            blue_foul_committed()
    elif any([key in COMBO for COMBO in timestart]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in timestart):
            Start(time_label)
    elif any([key in COMBO for COMBO in timepause]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in timepause):
            Stop()
    elif any([key in COMBO for COMBO in timerestart]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in timerestart):
            Reset(time_label)
def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)    
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    root.mainloop()
    listener.join()


root.mainloop()