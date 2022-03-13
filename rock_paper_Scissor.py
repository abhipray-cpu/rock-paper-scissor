import tkinter as tk
from tkinter import ttk
from math import *
from random import *
from windows import set_dpi_awareness
from PIL import Image,ImageTk
set_dpi_awareness()

class main_frame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Rock paper scissors game')
        self.geometry('400x400')
        self.resizable(False,False)
        container=frame()
        container.grid(row=0,column=0,sticky='nsew')

class frame(ttk.Frame):
    def __init__(self):
        super().__init__()
        self.option=tk.StringVar()
        self.winner=tk.StringVar()
        self.computerChoice=tk.StringVar()
        scissor_img = Image.open('scissor.jpg').resize((100,100))
        paper_img = Image.open('paper.jpeg').resize((100, 100))
        stone_img = Image.open('stone.jpg').resize((100, 100))

        photo_scissor = ImageTk.PhotoImage(scissor_img)
        photo_paper = ImageTk.PhotoImage(paper_img)
        photo_stone = ImageTk.PhotoImage(stone_img)

        label_scissor=ttk.Button(self,image=photo_scissor,text='Scissors',compound='right',command=self.result1)
        label_paper=ttk.Button(self,image=photo_paper,text='Paper',compound='right',command=self.result2)
        label_stone=ttk.Button(self,image=photo_stone,text='Rock',compound='right',command=self.result3)

        label_scissor.grid(row=0,column=0,padx=(150,150),pady=(10,50))
        label_paper.grid(row=1, column=0,padx=(150,150),pady=(0,50))
        label_stone.grid(row=2, column=0,padx=(150,150),pady=(0,50))
        frame=ttk.Frame(self)

        label_player_choice = ttk.Label(frame,text='You Chose')
        player_output=ttk.Label(frame,textvariable=self.option)
        label_computer_choice = ttk.Label(frame,text="Computer Chose")
        computer_output=ttk.Label(frame,textvariable=self.computerChoice)
        winner_label = ttk.Label(frame,text='Result')
        winner_output=ttk.Label(frame,textvariable=self.winner)

        label_player_choice.grid(row=0,column=0,padx=(10,40),pady=(10,10))
        label_computer_choice.grid(row=0,column=1,padx=(10,40),pady=(10,10))
        winner_label.grid(row=0,column=2,padx=(10,40),pady=(10,10))
        player_output.grid(row=1,column=0,padx=(10,40),pady=(10,10))
        computer_output.grid(row=1,column=1,padx=(10,40),pady=(10,10))
        winner_output.grid(row=1,column=2,padx=(10,40),pady=(10,10))
        frame.grid(row=3,column=0,sticky='nsew')



    def calculate(self):
        rand_number=randint(1,30)
        print(rand_number)
        computer_choice=''
        if rand_number in [1,4,7,10,13,16,19,22,25,28]:
            computer_choice = 'Scissor'
        elif rand_number in [2,5,8,11,14,17,20,23,26,29]:
            computer_choice = 'Paper'
        elif rand_number in [3,6,9,12,15,18,21,24,27,30]:
            computer_choice = 'Rock'

        print(computer_choice)
        self.computerChoice.set(computer_choice)
        player_choice=self.option.get()
        if player_choice == 'Scissor' and computer_choice == 'Scissor':
            self.winner.set('Draw')
        elif player_choice == 'Scissor' and computer_choice == 'Rock':
            self.winner.set('You Lost')
        elif player_choice == 'Scissor' and computer_choice == 'Paper':
            self.winner.set('You Won')
        if player_choice == 'Rock' and computer_choice == 'Rock':
            self.winner.set('Draw')
        elif player_choice == 'Rock' and computer_choice == 'Scissor':
            self.winner.set('You Won')
        elif player_choice == 'Rock' and computer_choice == 'Paper':
            self.winner.set('You Lost')
        if player_choice == 'Paper' and computer_choice == 'Paper':
            self.winner.set('Draw')
        elif player_choice == 'Paper' and computer_choice == 'Rock':
            self.winner.set('You Won')
        elif player_choice == 'Paper' and computer_choice == 'Scissor':
            self.winner.set('You Lost')

        print(self.winner.get())



    def result1(self):
        self.option.set('Scissor')
        self.calculate()
    def result2(self):
        self.option.set('Paper')
        self.calculate()
    def result3(self):
        self.option.set('Rock')
        self.calculate()









root=main_frame()
style = ttk.Style(root)  # Pass in which application this style is for.

# Get the themes available in your system
print(style.theme_names())
print(style.theme_use("xpnative"))
root.mainloop()