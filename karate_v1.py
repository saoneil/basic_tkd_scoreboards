import tkinter as tk
from datetime import datetime
from pynput import keyboard

def quit_me():
    print('quit')
    root.quit()
    root.destroy()
    quit()

root = tk.Tk()
root.title("PMA | Class Sparring")
root.protocol("WM_DELETE_WINDOW", quit_me)
root.geometry('1000x500')

counter = 0
running = False
red_score = 0
blue_score = 0

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
def single_point_score_blue():
    global blue_score
    blue_score += 1
    label_blue_score.config(text=blue_score)
def reset_all():
    global red_score
    global blue_score
    red_score = 0
    blue_score = 0
    label_red_score.config(text=red_score)
    label_blue_score.config(text=blue_score)

time_label = tk.Label(root, text="Ready", fg="black", font="Verdana 200 bold")
time_label.place(relx=0.5, rely=0.15, anchor='center')

start = tk.Button(root, text='Start', font="Verdana 20 bold", width=10, height=2, command=lambda: Start(time_label))
start.place(relx=0.5, rely=0.6, anchor='center')

stop = tk.Button(root, text='Stop', font="Verdana 20 bold", width=10, height=2, state='disabled', command=Stop)
stop.place(relx=0.5, rely=0.7, anchor='center')

reset = tk.Button(root, text='Reset', font="Verdana 20 bold", width=10, height=2, state='disabled', command=lambda: Reset(time_label))
reset.place(relx=0.5, rely=0.8, anchor='center')

reset_all = tk.Button(root, text='Reset Scores', font='verdana 20 bold', width=10, height=2, command=reset_all)
reset_all.place(relx=0.5, rely=0.9, anchor='center')



label_red_score = tk.Label(root, text=red_score, font='Verdana 400 bold', bg='red')
label_red_score.place(relx=0.2, rely=0.65, anchor='center')

label_blue_score = tk.Label(root, text=blue_score, font='Verdana 400 bold', bg='dodger blue')
label_blue_score.place(relx=0.8, rely=0.65, anchor='center')



COMBINATIONS = []
red = [{keyboard.KeyCode(char='r')}]
blue = [{keyboard.KeyCode(char='b')}]
timestart = [{keyboard.KeyCode(char='q')}]
timepause = [{keyboard.KeyCode(char='p')}]
timerestart = [{keyboard.KeyCode(char='l')}]
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