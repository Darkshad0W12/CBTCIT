import random
import tkinter as tk

window = tk.Tk()
window.title("G-A-M-E")

USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = ""

def choice_to_number(choice):
    rps = {'rock': 0, 'paper': 1, 'scissor': 2}
    return rps[choice]

def number_to_choice(number):
    rps = {0: 'rock', 1: 'paper', 2: 'scissor'}
    return rps[number]

def random_computer_choice():
    return random.choice(['rock', 'paper', 'scissor'])

def result(human_choice, comp_choice):
    global USER_SCORE
    global COMP_SCORE
    global USER_CHOICE
    global COMP_CHOICE

    USER_CHOICE = human_choice.lower()
    COMP_CHOICE = comp_choice.lower()

    user = choice_to_number(USER_CHOICE)
    comp = choice_to_number(COMP_CHOICE)

    result_text = ""
    if user == comp:
        result_text = "TIE"
    elif (user - comp) % 3 == 1:
        result_text = "YOU WIN"
        USER_SCORE += 1
    else:
        result_text = "Comp wins"
        COMP_SCORE += 1

    text_area.delete(1.0, tk.END)
    answer = f"YOUR CHOICE: {USER_CHOICE.capitalize()}\nComputer's Choice: {COMP_CHOICE.capitalize()}\nResult: {result_text}\nYour Score: {USER_SCORE}\nComputer Score: {COMP_SCORE}"
    text_area.insert(tk.END, answer)

def rock():
    comp_choice = random_computer_choice()
    result('rock', comp_choice)

def paper():
    comp_choice = random_computer_choice()
    result('paper', comp_choice)

def scissor():
    comp_choice = random_computer_choice()
    result('scissor', comp_choice)

# Configure grid weights to make elements expand to fill the screen
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)

button1 = tk.Button(text="Rock", bg="#68e884", command=rock)
button1.grid(row=1, sticky="nsew")  # Use sticky to expand buttons
button2 = tk.Button(text="Paper", bg="#fafcfc", command=paper)
button2.grid(row=2, sticky="nsew")
button3 = tk.Button(text="Scissor", bg="#59c5de", command=scissor)
button3.grid(row=3, sticky="nsew")

text_area = tk.Text(master=window, height=12, width=30, bg="#118b9c")
text_area.grid(row=4, sticky="nsew")

# Add padding to the buttons and text area
pad = 10
button1.grid(pady=pad)
button2.grid(pady=pad)
button3.grid(pady=pad)
text_area.grid(padx=pad, pady=pad)

window.mainloop()
