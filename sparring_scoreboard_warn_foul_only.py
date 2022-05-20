import tkinter as tk
from datetime import datetime
from pynput import keyboard


def quit_me():
    print('quit')
    root.quit()
    root.destroy()
    quit()

root = tk.Tk()
root.title("Performance Taekwon-Do | Team Sparring")
root.protocol("WM_DELETE_WINDOW", quit_me)

bg = tk.PhotoImage(file="bg_image.png")
main_title = tk.Label(root, image=bg)
main_title.place(x=0, y=0, relwidth=1, relheight=1)

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
red_warnings = 0
red_fouls = 0
blue_warnings = 0
blue_fouls = 0
round_counter = 0

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
def warn_red_inc():
    global red_warnings
    red_warnings += 1
    label_red_warnings.config(text=red_warnings)
def warn_red_dec():
    global red_warnings
    red_warnings -= 1
    label_red_warnings.config(text=red_warnings)
def warn_blue_inc():
    global blue_warnings
    blue_warnings += 1
    label_blue_warnings.config(text=blue_warnings)
def warn_blue_dec():
    global blue_warnings
    blue_warnings -= 1
    label_blue_warnings.config(text=blue_warnings)
def round_counter_inc():
    global round_counter
    round_counter += 1
    label_round_counter.config(text=round_counter)
def round_counter_dec():
    global round_counter
    round_counter -= 1
    label_round_counter.config(text=round_counter)
def red_foul_inc():
    global red_fouls
    red_fouls += 1
    label_red_fouls .config(text=red_fouls)
def red_foul_dec():
    global red_fouls
    red_fouls -= 1
    label_red_fouls .config(text=red_fouls)
def blue_foul_inc():
    global blue_fouls
    blue_fouls += 1
    label_blue_fouls .config(text=blue_fouls)
def blue_foul_dec():
    global blue_fouls
    blue_fouls -= 1
    label_blue_fouls .config(text=blue_fouls)
def reset_all():
    global red_warnings, blue_warnings, round_counter, red_fouls, blue_fouls
    red_warnings = 0
    blue_warnings = 0
    round_counter = 0
    red_fouls = 0
    blue_fouls = 0
    label_red_warnings.config(text=red_warnings)
    label_blue_warnings.config(text=blue_warnings)
    label_round_counter.config(text=round_counter)
    label_red_fouls.config(text=red_fouls)
    label_blue_fouls.config(text=blue_fouls)

time_label = tk.Label(root, text="Ready", bg='black', fg="white", font="Verdana 120 bold")
start = tk.Button(root, text='Start', font="Verdana 10 bold", width=10, height=1, command=lambda: Start(time_label))
stop = tk.Button(root, text='Stop', font="Verdana 10 bold", width=10, height=1, state='disabled', command=Stop)
reset = tk.Button(root, text='Reset', font="Verdana 10 bold", width=10, height=1, state='disabled', command=lambda: Reset(time_label))

label_red_warnings = tk.Label(root, text=red_warnings, font='Verdana 220 bold', bg='black', fg='white')
label_red_fouls = tk.Label(root, text=red_fouls, font='Verdana 150 bold', bg='black', fg='white')
label_blue_warnings = tk.Label(root, text=blue_warnings, font='Verdana 220 bold', bg='black', fg='white')
label_blue_fouls = tk.Label(root, text=blue_fouls, font='Verdana 150 bold', bg='black', fg='white')
label_round_counter = tk.Label(root, text=round_counter, font='Verdana 100 bold', bg='black', fg='white')
rw = tk.Label(root, text="Warnings", font='Verdana 10 bold', bg='black', fg='white')
bw = tk.Label(root, text="Warnings", font='Verdana 10 bold', bg='black', fg='white')
rf = tk.Label(root, text="Fouls", font='Verdana 10 bold', bg='black', fg='white')
bf = tk.Label(root, text="Fouls", font='Verdana 10 bold', bg='black', fg='white')
round = tk.Label(root, text="Round", font='Verdana 10 bold', bg='black', fg='white')

redwarninc = tk.Button(root, text="redwarning+", font='Verdana 5 bold', command=warn_red_inc, width=10, height=1)
redwarndec = tk.Button(root, text="redwarning-", font='Verdana 5 bold', command=warn_red_dec, width=10, height=1)
redfoulinc = tk.Button(root, text="redfoul+", font='Verdana 5 bold', command=red_foul_inc, width=10, height=1)
redfouldec = tk.Button(root, text="redfoul-", font='Verdana 5 bold', command=red_foul_dec, width=10, height=1)
bluewarninc = tk.Button(root, text="bluewarning+", font='Verdana 5 bold', command=warn_blue_inc, width=10, height=1)
bluewarndec = tk.Button(root, text="bluewarning-", font='Verdana 5 bold', command=warn_blue_dec, width=10, height=1)
bluefoulinc = tk.Button(root, text="bluefoul+", font='Verdana 5 bold', command=blue_foul_inc, width=10, height=1)
bluefouldec = tk.Button(root, text="bluefoul-", font='Verdana 5 bold', command=blue_foul_dec, width=10, height=1)
roundcounterinc = tk.Button(root, text="round+", font='Verdana 5 bold', command=round_counter_inc, width=10, height=1)
roundcounterdec = tk.Button(root, text="round-", font='Verdana 5 bold', command=round_counter_dec, width=10, height=1)
reset_all = tk.Button(root, text='Reset Scores', command=reset_all, width=15)

time_label.grid(row=1, column=3)
start.grid(row=6, column=3)
stop.grid(row=7, column=3)
reset.grid(row=8, column=3)
reset_all.grid(row=9, column=3)

label_red_warnings.grid(row=2, column=2)
label_red_fouls.grid(row=2, column=1)
label_blue_warnings.grid(row=2, column=4)
label_blue_fouls.grid(row=2, column=5)
label_round_counter.grid(row=2, column=3)

rw.place(relx=0.215, rely=0.20)
rf.place(relx=0.06, rely=0.24)
bw.place(relx=0.75, rely=0.20)
bf.place(relx=0.9175, rely=0.24)
round.place(relx=0.4875, rely=0.32)

redwarninc.place(relx=0.22, rely=0.27)
redwarndec.place(relx=0.22, rely=0.635)
redfoulinc.place(relx=0.055, rely=0.325)
redfouldec.place(relx=0.055, rely=0.58)
bluewarninc.place(relx=0.755, rely=0.27)
bluewarndec.place(relx=0.755, rely=0.635)
bluefoulinc.place(relx=0.915, rely=0.325)
bluefouldec.place(relx=0.915, rely=0.58)
roundcounterinc.place(relx=0.486, rely=0.365)
roundcounterdec.place(relx=0.486, rely=0.54)


COMBINATIONS = []
red_inc = [{keyboard.KeyCode(char='r')}]
blue_inc = [{keyboard.KeyCode(char='b')}]
red_dec = [{keyboard.KeyCode(char='t')}]
blue_dec = [{keyboard.KeyCode(char='n')}]
tie_inc = [{keyboard.KeyCode(char='d')}]
tie_dec = [{keyboard.KeyCode(char='f')}]
timestart = [{keyboard.KeyCode(char='q')}]
timepause = [{keyboard.KeyCode(char='a')}]
timerestart = [{keyboard.KeyCode(char='z')}]
current = set()

def on_press(key):
    if any([key in COMBO for COMBO in red_inc]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in red_inc):
            warn_red_inc()
    elif any([key in COMBO for COMBO in blue_inc]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in blue_inc):
            warn_blue_inc()
    elif any([key in COMBO for COMBO in red_dec]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in red_dec):
            warn_red_dec()
    elif any([key in COMBO for COMBO in blue_dec]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in blue_dec):
            warn_blue_dec()
    elif any([key in COMBO for COMBO in tie_inc]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in tie_inc):
            round_counter_inc()
    elif any([key in COMBO for COMBO in tie_dec]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in tie_dec):
            round_counter_dec()
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