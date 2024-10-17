import random
import time
import tkinter as tk
from tkinter import messagebox

num = chances = tries = 0
start_time = None

def start():
    global num, chances, tries, start_time
    tries = 0
    
    lvl = diff_var.get()   
    if lvl == "1":
        chances = 10
    elif lvl == "2":
        chances = 5
    elif lvl == "3":
        chances = 3
    
    num = random.randint(1, 100)
    start_time = time.time()
    
    guess_frame.pack(pady=10)
    action_frame.pack(pady=10)
    result_lbl.config(text="")
    guess_entry.focus()

def check_guess():
    global tries, chances
    if chances <= 0:
        messagebox.showinfo("Game Over", "No more chances left!")
        return

    try:
        user_guess = int(guess_entry.get())
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid number!")
        return

    tries += 1
    chances -= 1

    if user_guess == num:
        time_taken = time.time() - start_time
        messagebox.showinfo("Congratulations!", f"You guessed the number {num} in {tries} attempts! Time taken: {int(time_taken)} seconds.")
        reset()
    elif user_guess < num:
        result_lbl.config(text=f"Incorrect! The number is greater than {user_guess}. Chances left: {chances}")
    else:
        result_lbl.config(text=f"Incorrect! The number is less than {user_guess}. Chances left: {chances}")

    if chances <= 0:
        messagebox.showinfo("Game Over", f"You're out of chances! The number was {num}.")
        reset()

def get_hint():
    global chances
    if chances <= 0:
        messagebox.showinfo("Game Over", "No more chances left!")
        return

    hint_msg = "The number is even." if num % 2 == 0 else "The number is odd."

    chances -= 1
    messagebox.showinfo("Hint", f"{hint_msg} Chances left: {chances}")

    if chances <= 0:
        messagebox.showinfo("Game Over", f"You're out of chances! The number was {num}.")
        reset()

def reset():
    guess_frame.pack_forget()
    action_frame.pack_forget()
    guess_entry.delete(0, tk.END)
    result_lbl.config(text="")

root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x400")
root.config(bg="#2c3e50")


title_lbl = tk.Label(root, text="Number Guessing Game", font=("Helvetica", 18, "bold"), fg="#ecf0f1", bg="#2c3e50")
title_lbl.pack(pady=10)


instr_lbl = tk.Label(root, text="I'm thinking of a number between 1 and 100.", font=("Helvetica", 12), fg="#ecf0f1", bg="#2c3e50")
instr_lbl.pack(pady=5)


diff_frame = tk.Frame(root, bg="#34495e", padx=10, pady=10, relief="groove", bd=2)
diff_frame.pack(pady=10)

diff_lbl = tk.Label(diff_frame, text="Select Difficulty Level:", font=("Helvetica", 12), fg="#ecf0f1", bg="#34495e")
diff_lbl.pack()

diff_var = tk.StringVar(value="1")
tk.Radiobutton(diff_frame, text="Easy (10 chances)", variable=diff_var, value="1", bg="#34495e", fg="#ecf0f1", selectcolor="#2c3e50").pack(anchor="w")
tk.Radiobutton(diff_frame, text="Medium (5 chances)", variable=diff_var, value="2", bg="#34495e", fg="#ecf0f1", selectcolor="#2c3e50").pack(anchor="w")
tk.Radiobutton(diff_frame, text="Hard (3 chances)", variable=diff_var, value="3", bg="#34495e", fg="#ecf0f1", selectcolor="#2c3e50").pack(anchor="w")

start_btn = tk.Button(diff_frame, text="Start Game", command=start, bg="#e67e22", fg="#ecf0f1", font=("Helvetica", 12), padx=10)
start_btn.pack(pady=10)


guess_frame = tk.Frame(root, bg="#34495e", padx=10, pady=10, relief="groove", bd=2) 

guess_lbl = tk.Label(guess_frame, text="Enter your guess:", font=("Helvetica", 12), fg="#ecf0f1", bg="#34495e")
guess_lbl.pack(pady=5)

guess_entry = tk.Entry(guess_frame, font=("Helvetica", 12))
guess_entry.pack()


action_frame = tk.Frame(root, bg="#34495e", padx=10, pady=10, relief="groove", bd=2) 

guess_btn = tk.Button(action_frame, text="Submit Guess", command=check_guess, bg="#27ae60", fg="#ecf0f1", font=("Helvetica", 12), padx=10)
guess_btn.pack(side="left", padx=5)

hint_btn = tk.Button(action_frame, text="Get a Hint", command=get_hint, bg="#2980b9", fg="#ecf0f1", font=("Helvetica", 12), padx=10)
hint_btn.pack(side="left", padx=5)


result_lbl = tk.Label(root, text="", font=("Helvetica", 12), fg="#ecf0f1", bg="#2c3e50") 
result_lbl.pack(pady=10)


root.mainloop()
