import tkinter as tk
import random

p1 = 0
p2 = 0

x = 0

val3 = 0
val6 = 0

root2 = tk.Tk()
root2.geometry("300x300")
root2.title("Authentication")

user = tk.Label(root2, text = "Enter a username:")
user.pack()
user_entry = tk.Entry(root2)
user_entry.pack()
pass1 = tk.Label(root2, text = "Enter a password:")
pass1.pack()
pass1_entry = tk.Entry(root2)
pass1_entry.pack()

wrong = tk.Label(root2, text = "")

def submit():
    user_str = user_entry.get()
    pass1_str = pass1_entry.get()
    if len(user_str) > 12:
        wrong.configure(text = "username too long, try entering one under 12 characters", fg = "red")
        wrong.pack()
    if  pass1_str != "1234":
        wrong.configure(text = "password is worng, try entering the correct one", fg = "red")
        wrong.pack()
    elif len(user_str) < 12 and pass1_str == "1234":
        playB.pack()
    
submit1 = tk.Button(root2, text = "submit", command = submit)
submit1.pack()


def play():
    root = tk.Tk()
    root.geometry("400x400")
    root.title("dice game")


    dice = ("\u2680","\u2681","\u2682","\u2683","\u2684","\u2685")

    label = tk.Label(root, text = "", font=("Helvetica", 260))
    label2 = tk.Label(root, text = "", font=("Helvetica", 260))


    def roll_dice():
        p1_Dice1 = random.choice(dice)
        p1_Dice2 = random.choice(dice)
        p1_Dice3 = random.choice(dice)
        p1_Dice4 = random.choice(dice)
        p1_Dice5 = random.choice(dice)
        dice1 = (p1_Dice2, p1_Dice1, p1_Dice3, p1_Dice4, p1_Dice5)
        label2.pack_forget()
        label.configure(text=dice1)
        label.pack()
    def roll_dice2():
        p1_Dice1 = random.choice(dice)
        p1_Dice2 = random.choice(dice)
        p1_Dice3 = random.choice(dice)
        p1_Dice4 = random.choice(dice)
        dice2 = (p1_Dice2, p1_Dice1, p1_Dice3, p1_Dice4)
        label2.pack_forget()
        label.configure(text=dice2)
        label.pack()
    def roll_dice3():
        p1_Dice1 = random.choice(dice)
        p1_Dice2 = random.choice(dice)
        p1_Dice3 = random.choice(dice)
        dice3 = (p1_Dice2, p1_Dice1, p1_Dice3)
        label2.pack_forget()
        label.configure(text=dice3)
        label.pack()
    def roll_dice4():
        p1_Dice1 = random.choice(dice)
        p1_Dice2 = random.choice(dice)
        dice4 = (p1_Dice2, p1_Dice1)
        label2.pack_forget()
        label.configure(text=dice4)
        label.pack()
    def roll_dice5():
        p1_Dice1 = random.choice(dice)
        dice5 = (p1_Dice1)
        label2.pack_forget()
        label.configure(text=dice5)
        label.pack()
        
    button = tk.Button(root, text = "Roll 5 dice", fg = "green", command = roll_dice)
    button.pack()
    button3 = tk.Button(root, text = "Roll 4 dice", fg = "green", command = roll_dice2)
    button3.pack()
    button4 = tk.Button(root, text = "Roll 3 dice", fg = "green", command = roll_dice3)
    button4.pack()
    button5 = tk.Button(root, text = "Roll 2 dice", fg = "green", command = roll_dice4)
    button5.pack()
    button6 = tk.Button(root, text = "Roll 1 dice", fg = "green", command = roll_dice5)
    button6.pack()

    
    root.mainloop()

playB = tk.Button(root2, text = "Play", command = play)

root2.mainloop()
