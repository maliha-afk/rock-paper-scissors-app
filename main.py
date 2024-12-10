from tkinter import *
import random

screen = Tk()
screen.title("Rock Paper Scissors")
screen.geometry("500x500")
screen.config(bg="purple3")

Label(screen,text="welcome to rock paper scissors app",font=("Alice",15,"bold"),bg="purple3",fg="black").grid(row=0,column=1)
Label(screen,text="",font=("Alice",15,"bold"),bg="purple3",fg="black").grid(row=1,column=1)
Label(screen,text="",font=("Alice",15,"bold"),bg="purple3",fg="black").grid(row=3,column=1)

def play_round(user_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        result = "You win!"
    
    else:
        result = "Computer wins!"
    
    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")

rock_button = Button(screen, text="Rock",font=("Alice",10,"bold"),bg="purple1",fg="black", command=lambda: play_round("rock"))
rock_button.grid(row=2,column=0)

paper_button = Button(screen, text="Paper",font=("Alice",10,"bold"),bg="purple1",fg="black", command=lambda: play_round("paper"))
paper_button.grid(row=2,column=1)

scissors_button = Button(screen, text="Scissors",font=("Alice",10,"bold"),bg="purple1",fg="black", command=lambda: play_round("scissors"))
scissors_button.grid(row=2,column=3)

Label(screen,text="",font=("Alice",15,"bold"),bg="purple3",fg="black").grid(row=3,column=1)
result_label = Label(screen, text="",font=("Alice",15,"bold"),bg="purple3",fg="black")
result_label.grid(row=3,column=1)

screen.mainloop()

