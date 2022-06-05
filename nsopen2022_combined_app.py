import random
import tkinter as tk
from datetime import datetime
from pynput import keyboard
from tkinter import ttk

window_width = 1918
window_height = 1030

# tab 1
patvar = 0
pattern1 = ""
pattern2 = ""

# tab 2
counter = 0
running = False
red_warnings = 0
red_fouls = 0
blue_warnings = 0
blue_fouls = 0
round_counter = 0

# tab 3
counter3 = 0
running3 = False
red_score = 0
blue_score = 0
tie_score = 0

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        nb = ttk.Notebook(root, width=window_width, height=window_height)
        nb.grid(row=0, column=0)
        tab1 = ttk.Frame(nb)
        nb.add(tab1, text='Black Belt Patterns')
        tab2 = ttk.Frame(nb)
        nb.add(tab2, text='Sparring - Time, Warnings, Fouls')
        tab3 = ttk.Frame(nb)
        nb.add(tab3, text='Team Sparring Time, Tally')
        
        
        ###
        # TAB 1 - Black Belt Patterns
        ###        

        firstdanlist = [
                    'Chon-Ji', #0
                    'Dan-Gun', #1
                    'Do-San', #2
                    'Won-Hyo', #3
                    'Yul-Gok', #4
                    'Joong-Gun', #5
                    'Toi-Gye', #6
                    'Hwa-Rang', #7
                    'Choong-Moo', #8
                    'Kwang-Gae', #9
                    'Po-Eun', #10
                    'Gae-Baek', #11
]
        seconddanlist = [
                    "Chon-Ji", #0
                    "Dan-Gun", #1
                    "Do-San", #2
                    "Won-Hyo", #3
                    "Yul-Gok", #4
                    "Joong-Gun", #5
                    "Toi-Gye", #6
                    "Hwa-Rang", #7
                    "Choong-Moo", #8
                    "Kwang-Gae", #9
                    "Po-Eun", #10
                    "Gae-Baek", #11
                    "Eui-Am", #12 
                    "Choong-Jang", #13
                    "Juche", #14
        ]
        thirddanlist = [
                    "Chon-Ji", #0
                    "Dan-Gun", #1
                    "Do-San", #2
                    "Won-Hyo", #3
                    "Yul-Gok", #4
                    "Joong-Gun", #5
                    "Toi-Gye", #6
                    "Hwa-Rang", #7
                    "Choong-Moo", #8
                    "Kwang-Gae", #9
                    "Po-Eun", #10
                    "Gae-Baek", #11
                    "Eui-Am", #12 
                    "Choong-Jang", #13
                    "Juche", #14
                    "Sam-Il", #15
                    "Yoo-Sin", #16
                    "Choi-Yong", #17
        ]
        fourthdanlist = [
            "Chon-Ji", #0
            "Dan-Gun", #1
            "Do-San", #2
            "Won-Hyo", #3
            "Yul-Gok", #4
            "Joong-Gun", #5
            "Toi-Gye", #6
            "Hwa-Rang", #7
            "Choong-Moo", #8
            "Kwang-Gae", #9
            "Po-Eun", #10
            "Gae-Baek", #11
            "Eui-Am", #12 
            "Choong-Jang", #13
            "Juche", #14
            "Sam-Il", #15
            "Yoo-Sin", #16
            "Choi-Yong", #17
            "Yong-Gae", #18
            "Ul-Ji", #19
            "Moon-Moo" #20
]

        pattern_string = "          "
        pattern_label = tk.Label(tab1, text=pattern_string, font = "Verdana 150 bold", bg = "white")
        pattern_label.place(relx=0.5, rely=0.2, anchor='center')

        def firstdan():
            global pattern1, pattern2, patvar
            copylist = firstdanlist.copy()
            num1 = random.randint(9,11)
            pattern1 = copylist[num1]
            print(copylist[num1])
            copylist.remove(copylist[num1])
            num2 = random.randint(0, 10)
            pattern2 = copylist[num2]
            print(copylist[num2])
        def seconddan():
            global pattern1, pattern2, patvar
            copylist = seconddanlist.copy()
            num1 = random.randint(12,14)
            pattern1 = copylist[num1]
            print(copylist[num1])
            copylist.remove(copylist[num1])
            num2 = random.randint(0, 13)
            pattern2 = copylist[num2]
            print(copylist[num2])
        def thirddan():
            global pattern1, pattern2, patvar
            copylist = thirddanlist.copy()
            num1 = random.randint(15,17)
            pattern1 = copylist[num1]
            print(copylist[num1])
            copylist.remove(copylist[num1])
            num2 = random.randint(0, 16)
            pattern2 = copylist[num2]
            print(copylist[num2])
        def fourthdan():
            global pattern1, pattern2, patvar
            copylist = fourthdanlist.copy()
            num1 = random.randint(18,20)
            pattern1 = copylist[num1]
            print(copylist[num1])
            copylist.remove(copylist[num1])
            num2 = random.randint(0, 19)
            pattern2 = copylist[num2]
            print(copylist[num2])
        def display():
            global patvar
            if patvar == 0:
                pattern_label.config(text=pattern1)
                patvar = 1
            elif patvar == 1:
                pattern_label.config(text=pattern2)
                patvar = 0

        firstdan1 = tk.Button(tab1, text="1st Dan - Generate", command = firstdan, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
        firstdan1.place(relx=0.05, rely=0.90, anchor='center')
        firstdan2 = tk.Button(tab1, text="Display", command = display, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
        firstdan2.place(relx=0.05, rely=0.95, anchor='center')
        seconddan1 = tk.Button(tab1, text="2nd Dan - Generate", command = seconddan, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
        seconddan1.place(relx=0.35, rely=0.90, anchor='center')
        seconddan2 = tk.Button(tab1, text="Display", command = display, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
        seconddan2.place(relx=0.35, rely=0.95, anchor='center')
        thirddan1 = tk.Button(tab1, text="3rd Dan - Generate", command = thirddan, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
        thirddan1.place(relx=0.65, rely=0.90, anchor='center')
        thirddan2 = tk.Button(tab1, text="Display", command = display, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
        thirddan2.place(relx=0.65, rely=0.95, anchor='center')
        fourthdan1 = tk.Button(tab1, text="4th-6th Dan - Generate", command = fourthdan, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
        fourthdan1.place(relx=0.95, rely=0.90, anchor='center')
        fourthdan2 = tk.Button(tab1, text="Display", command = display, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
        fourthdan2.place(relx=0.95, rely=0.95, anchor='center')
        
        
        ###
        # TAB 2 - Sparring - Time, Warnings, Fouls
        ###
        
        # bg = tk.PhotoImage(file="bg_image.png")
        # main_title = tk.Label(tab2, image=bg)
        # main_title.place(x=0, y=0, relwidth=1, relheight=1)

        tab2.grid_columnconfigure(1,weight=1)
        tab2.grid_columnconfigure(2,weight=1)
        tab2.grid_columnconfigure(3,weight=1)
        tab2.grid_columnconfigure(4,weight=1)
        tab2.grid_columnconfigure(5,weight=1)
        tab2.grid_rowconfigure(0,weight=1)
        tab2.grid_rowconfigure(1,weight=1)
        tab2.grid_rowconfigure(2,weight=1)
        tab2.grid_rowconfigure(3,weight=1)
        tab2.grid_rowconfigure(4,weight=1)
        tab2.grid_rowconfigure(5,weight=1)
        tab2.grid_rowconfigure(6,weight=1)
        tab2.grid_rowconfigure(7,weight=1)
        tab2.grid_rowconfigure(8,weight=1)

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

        time_label = tk.Label(tab2, text="Ready", bg='black', fg="white", font="Verdana 120 bold")
        start = tk.Button(tab2, text='Start', font="Verdana 10 bold", width=10, height=1, command=lambda: Start(time_label))
        stop = tk.Button(tab2, text='Stop', font="Verdana 10 bold", width=10, height=1, state='disabled', command=Stop)
        reset = tk.Button(tab2, text='Reset', font="Verdana 10 bold", width=10, height=1, state='disabled', command=lambda: Reset(time_label))

        label_red_warnings = tk.Label(tab2, text=red_warnings, font='Verdana 220 bold', bg='black', fg='white')
        label_red_fouls = tk.Label(tab2, text=red_fouls, font='Verdana 150 bold', bg='black', fg='white')
        label_blue_warnings = tk.Label(tab2, text=blue_warnings, font='Verdana 220 bold', bg='black', fg='white')
        label_blue_fouls = tk.Label(tab2, text=blue_fouls, font='Verdana 150 bold', bg='black', fg='white')
        label_round_counter = tk.Label(tab2, text=round_counter, font='Verdana 100 bold', bg='black', fg='white')
        rw = tk.Label(tab2, text="Warnings", font='Verdana 10 bold', bg='black', fg='white')
        bw = tk.Label(tab2, text="Warnings", font='Verdana 10 bold', bg='black', fg='white')
        rf = tk.Label(tab2, text="Fouls", font='Verdana 10 bold', bg='black', fg='white')
        bf = tk.Label(tab2, text="Fouls", font='Verdana 10 bold', bg='black', fg='white')
        round = tk.Label(tab2, text="Round", font='Verdana 10 bold', bg='black', fg='white')

        redwarninc = tk.Button(tab2, text="redwarning+", font='Verdana 5 bold', command=warn_red_inc, width=10, height=1)
        redwarndec = tk.Button(tab2, text="redwarning-", font='Verdana 5 bold', command=warn_red_dec, width=10, height=1)
        redfoulinc = tk.Button(tab2, text="redfoul+", font='Verdana 5 bold', command=red_foul_inc, width=10, height=1)
        redfouldec = tk.Button(tab2, text="redfoul-", font='Verdana 5 bold', command=red_foul_dec, width=10, height=1)
        bluewarninc = tk.Button(tab2, text="bluewarning+", font='Verdana 5 bold', command=warn_blue_inc, width=10, height=1)
        bluewarndec = tk.Button(tab2, text="bluewarning-", font='Verdana 5 bold', command=warn_blue_dec, width=10, height=1)
        bluefoulinc = tk.Button(tab2, text="bluefoul+", font='Verdana 5 bold', command=blue_foul_inc, width=10, height=1)
        bluefouldec = tk.Button(tab2, text="bluefoul-", font='Verdana 5 bold', command=blue_foul_dec, width=10, height=1)
        roundcounterinc = tk.Button(tab2, text="round+", font='Verdana 5 bold', command=round_counter_inc, width=10, height=1)
        roundcounterdec = tk.Button(tab2, text="round-", font='Verdana 5 bold', command=round_counter_dec, width=10, height=1)
        reset_all = tk.Button(tab2, text='Reset Scores', command=reset_all, width=15)

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

        redwarninc.place(relx=0.22, rely=0.275)
        redwarndec.place(relx=0.22, rely=0.633)
        redfoulinc.place(relx=0.056, rely=0.33)
        redfouldec.place(relx=0.056, rely=0.577)
        bluewarninc.place(relx=0.755, rely=0.275)
        bluewarndec.place(relx=0.755, rely=0.633)
        bluefoulinc.place(relx=0.915, rely=0.33)
        bluefouldec.place(relx=0.915, rely=0.577)
        roundcounterinc.place(relx=0.486, rely=0.368)
        roundcounterdec.place(relx=0.486, rely=0.54)
        
        
        ###
        # TAB 3 - Team Sparring Time, Tally
        ###

        # bg = tk.PhotoImage(file="bg_image.png")
        # main_title = tk.Label(tab3, image=bg)
        # main_title.place(x=0, y=0, relwidth=1, relheight=1)

        tab3.grid_columnconfigure(1,weight=1)
        tab3.grid_columnconfigure(2,weight=1)
        tab3.grid_columnconfigure(3,weight=1)
        tab3.grid_columnconfigure(4,weight=1)
        tab3.grid_columnconfigure(5,weight=1)
        tab3.grid_rowconfigure(0,weight=1)
        tab3.grid_rowconfigure(1,weight=1)
        tab3.grid_rowconfigure(2,weight=1)
        tab3.grid_rowconfigure(3,weight=1)
        tab3.grid_rowconfigure(4,weight=1)
        tab3.grid_rowconfigure(5,weight=1)
        tab3.grid_rowconfigure(6,weight=1)
        tab3.grid_rowconfigure(7,weight=1)
        tab3.grid_rowconfigure(8,weight=1)

        def counter_label3(label3):
            def count3():
                if running3:
                    global counter3
                    tt = datetime.fromtimestamp(counter3)
                    string3 = tt.strftime("%M:%S")
                    display = string3
                    label3.config(text=display)
                    label3.after(1000, count3)
                    counter3 += 1
            count3()
        def Start3(label3):
            global running3
            running3 = True
            counter_label3(label3)
            start3['state'] = 'disabled'
            stop3['state'] = 'normal'
            reset3['state'] = 'normal'
        def Stop3():
            global running3
            start3['state'] = 'normal'
            stop3['state'] = 'disabled'
            reset3['state'] = 'normal'
            running3 = False
        def Reset3(label3):
            global counter3
            counter3 = 0
            if running3 == False:
                reset3['state'] = 'disabled'
                label3['text'] = 'Ready'
            else:
                label3['text'] = 'Starting...'
        def score_red_inc():
            global red_score
            red_score += 1
            label_red_score.config(text=red_score)
        def score_red_dec():
            global red_score
            red_score -= 1
            label_red_score.config(text=red_score)
        def score_blue_inc():
            global blue_score
            blue_score += 1
            label_blue_score.config(text=blue_score)
        def score_blue_dec():
            global blue_score
            blue_score -= 1
            label_blue_score.config(text=blue_score)
        def score_tie_inc():
            global tie_score
            tie_score += 1
            label_tie_score.config(text=tie_score)
        def score_tie_dec():
            global tie_score
            tie_score -= 1
            label_tie_score.config(text=tie_score)
        def reset_all():
            global red_score, blue_score, tie_score
            red_score = 0
            blue_score = 0
            tie_score = 0
            label_red_score.config(text=red_score)
            label_blue_score.config(text=blue_score)
            label_tie_score.config(text=tie_score)

        time_label3 = tk.Label(tab3, text="Ready", bg='black', fg="white", font="Verdana 150 bold")
        start3 = tk.Button(tab3, text='Start', font="Verdana 10 bold", width=10, height=2, command=lambda: Start3(time_label3))
        stop3 = tk.Button(tab3, text='Stop', font="Verdana 10 bold", width=10, height=2, state='disabled', command=Stop3)
        reset3 = tk.Button(tab3, text='Reset', font="Verdana 10 bold", width=10, height=2, state='disabled', command=lambda: Reset3(time_label3))
        
        label_red_score = tk.Label(tab3, text=red_score, font='Verdana 250 bold', bg='black', fg='white')
        label_blue_score = tk.Label(tab3, text=blue_score, font='Verdana 250 bold', bg='black', fg='white')
        label_tie_score = tk.Label(tab3, text=tie_score, font='Verdana 160 bold', bg='black', fg='white')
        redscoreinc = tk.Button(tab3, text="+1 point", font='Verdana 10 bold', command=score_red_inc, width=7, height=1)
        redscoredec = tk.Button(tab3, text="-1 point", font='Verdana 10 bold', command=score_red_dec, width=7, height=1)
        bluescoreinc = tk.Button(tab3, text="+1 point", font='Verdana 10 bold', command=score_blue_inc, width=7, height=1)
        bluescoredec = tk.Button(tab3, text="-1 point", font='Verdana 10 bold', command=score_blue_dec, width=7, height=1)
        tiescoreinc = tk.Button(tab3, text="+1 point", font='Verdana 10 bold', command=score_tie_inc, width=7, height=1)
        tiescoredec = tk.Button(tab3, text="-1 point", font='Verdana 10 bold', command=score_tie_dec, width=7, height=1)
        reset_all = tk.Button(tab3, text='Reset Scores', command=reset_all, width=15)


        time_label3.grid(row=1, column=3)
        start3.grid(row=6, column=3)
        stop3.grid(row=7, column=3)
        reset3.grid(row=8, column=3)
        reset_all.grid(row=9, column=3)
        label_red_score.grid(row=2, column=2)
        label_blue_score.grid(row=2, column=4)
        label_tie_score.grid(row=2, column=3)

        redscoreinc.place(relx=0.18, rely=0.283, anchor='center')
        redscoredec.place(relx=0.18, rely=0.698, anchor='center')
        bluescoreinc.place(relx=0.82, rely=0.283, anchor='center')
        bluescoredec.place(relx=0.82, rely=0.698, anchor='center')
        tiescoreinc.place(relx=0.5, rely=0.353, anchor='center')
        tiescoredec.place(relx=0.5, rely=0.628, anchor='center')
        
                
        
if __name__ == "__main__":
    root = tk.Tk()
    ttk.Style().theme_use('default')
    root.title("Performance Taekwon-Do | NS Open Championship")
    root.minsize(width=window_width, height=window_height)
    MainApplication(root)
    root.mainloop()