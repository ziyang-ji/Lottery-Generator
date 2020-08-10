#!/usr/bin/env python3
#TK_SILENCE_DEPRECATION=1
import tkinter as tk
import threading
from time import sleep
from tkinter import messagebox
import pandas as pd
import numpy as np
from tkmacosx import Button

weights = []

df = pd.read_excel('challenge.xlsx')

beginner = df['Beginner'].dropna().values.tolist()
advanced = df['Advanced'].dropna().values.tolist()

complete = beginner + advanced
division = 1 / (len(beginner) + len(advanced) * 2)
weights += len(beginner) * [division]
weights += len(advanced) * [2 * division]

# print("complete: ", complete)
# print("beginner: ", beginner)
# print("advanced: ", advanced)

# print("Weights: ", end='')
# print(weights)

window = tk.Tk()
window.title('Lottery')
window.minsize(1000, 600)

btn_list = []
for i in range(len(complete)):	
    button = Button(window, text=complete[i], bg='lightblue', fg='black', borderless=1)
    button.pack()
    btn_list.append(button)
    y, x = divmod(i, 7)
    button.place(x=100+x*120, y=100+y*120, width=100, height=80)

def round():
    if btn_start['text'] == 'START':
        btn_start['text'] = 'STOP'
    else:
        btn_start['text'] = 'START'
        return

    while True:
        randomlist = np.random.choice(btn_list, 4, False, weights)
        for b in randomlist:
            b['bg'] = 'red'

        if btn_start['text'] == 'START':
            tk.messagebox.showinfo('Winners!', message='Congrats!\n{} {} {} {}'.format(randomlist[0]['text'], randomlist[1]['text'], randomlist[2]['text'], randomlist[3]['text']))
            break

        sleep(0.1)
        for x in btn_list:
            x['bg'] = 'lightblue'


def newtask():
    t = threading.Thread(target=round)
    t.start()

btn_start = tk.Button(window, text='START', bg='white', fg='black', command=newtask)
btn_start.place(x=400, y=450, width=200, height=80)

window.mainloop()



