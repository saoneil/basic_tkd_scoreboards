import random
import tkinter as tk

window = tk.Tk()
window.minsize(width=720, height=360)

patvar = 0
pattern1 = ""
pattern2 = ""

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
pattern_label = tk.Label(window, text=pattern_string, font = "Verdana 100 bold", bg = "white")
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

firstdan1 = tk.Button(window, text="1st Dan - Generate", command = firstdan, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
firstdan1.place(relx=0.05, rely=0.90, anchor='center')
firstdan2 = tk.Button(window, text="Display", command = display, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
firstdan2.place(relx=0.05, rely=0.95, anchor='center')
seconddan1 = tk.Button(window, text="2nd Dan - Generate", command = seconddan, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
seconddan1.place(relx=0.35, rely=0.90, anchor='center')
seconddan2 = tk.Button(window, text="Display", command = display, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
seconddan2.place(relx=0.35, rely=0.95, anchor='center')
thirddan1 = tk.Button(window, text="3rd Dan - Generate", command = thirddan, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
thirddan1.place(relx=0.65, rely=0.90, anchor='center')
thirddan2 = tk.Button(window, text="Display", command = display, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
thirddan2.place(relx=0.65, rely=0.95, anchor='center')
fourthdan1 = tk.Button(window, text="4th-6th Dan - Generate", command = fourthdan, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
fourthdan1.place(relx=0.95, rely=0.90, anchor='center')
fourthdan2 = tk.Button(window, text="Display", command = display, width=19, height=2, fg="white", bg = "black", font="Verdana 10 bold")
fourthdan2.place(relx=0.95, rely=0.95, anchor='center')



window.mainloop()