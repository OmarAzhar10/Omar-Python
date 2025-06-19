import tkinter as tk
import random

# Initialize scores and match mode
player_score = 0
computer_score = 0
rounds_to_play = 5

# Function to decide the winner and update UI
def play(user_choice):
    global player_score, computer_score
    
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You Win!"
        player_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(text=f"🎮 You: {user_choice}\n🖥️ Computer: {computer_choice}\n➡️ {result}")
    score_label.config(text=f"🏆 Scores - You: {player_score} | Computer: {computer_score}")
    check_match_end()

# Check for match end
def check_match_end():
    if player_score >= rounds_to_play:
        result_label.config(text=f"🎉 You won the match! 🎉")
        disable_buttons()
    elif computer_score >= rounds_to_play:
        result_label.config(text=f"💻 Computer won the match! 💻")
        disable_buttons()

# Disable choice buttons after match end
def disable_buttons():
    rock_button.config(state="disabled")
    paper_button.config(state="disabled")
    scissors_button.config(state="disabled")

# Reset the game
def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    result_label.config(text="Let's Play!")
    score_label.config(text=f"🏆 Scores - You: 0 | Computer: 0")
    rock_button.config(state="normal")
    paper_button.config(state="normal")
    scissors_button.config(state="normal")

# Set match mode (5 or 10 rounds)
def set_match(rounds):
    global rounds_to_play
    rounds_to_play = rounds
    reset_game()

# Create main window
window = tk.Tk()
window.title("✨ Rock Paper Scissors ✨")
window.geometry("400x500")
window.configure(bg="#f8f1f1")

# Title label
title_label = tk.Label(window, text="ROCK PAPER SCISSORS", font=("Helvetica", 20, "bold"), fg="#2c3e50", bg="#f8f1f1")
title_label.pack(pady=20)

# Match mode selection
mode_frame = tk.Frame(window, bg="#f8f1f1")
mode_frame.pack(pady=5)

tk.Label(mode_frame, text="Select Match Mode: ", font=("Helvetica", 12), bg="#f8f1f1").pack(side="left")
tk.Button(mode_frame, text="Best of 5", font=("Helvetica", 11), bg="#dff9fb", command=lambda: set_match(5)).pack(side="left", padx=5)
tk.Button(mode_frame, text="Best of 10", font=("Helvetica", 11), bg="#f9ca24", command=lambda: set_match(10)).pack(side="left", padx=5)

# Frame for buttons
button_frame = tk.Frame(window, bg="#f8f1f1")
button_frame.pack(pady=20)

# Choice buttons
rock_button = tk.Button(button_frame, text="🪨 Rock", width=12, height=2, bg="#c7ecee", font=("Helvetica", 14, "bold"), command=lambda: play('Rock'))
rock_button.grid(row=0, column=0, padx=10, pady=5)

paper_button = tk.Button(button_frame, text="📄 Paper", width=12, height=2, bg="#dff9fb", font=("Helvetica", 14, "bold"), command=lambda: play('Paper'))
paper_button.grid(row=0, column=1, padx=10, pady=5)

scissors_button = tk.Button(button_frame, text="✂️ Scissors", width=12, height=2, bg="#f9ca24", font=("Helvetica", 14, "bold"), command=lambda: play('Scissors'))
scissors_button.grid(row=0, column=2, padx=10, pady=5)

# Result label
result_label = tk.Label(window, text="Let's Play!", font=("Helvetica", 16), fg="#34495e", bg="#f8f1f1")
result_label.pack(pady=20)

# Score label
score_label = tk.Label(window, text="🏆 Scores - You: 0 | Computer: 0", font=("Helvetica", 13), fg="#30336b", bg="#f8f1f1")
score_label.pack(pady=10)

# Reset button
reset_button = tk.Button(window, text="🔄 Reset Game", width=20, height=2, bg="#ff7979", fg="white", font=("Helvetica", 12, "bold"), command=reset_game)
reset_button.pack(pady=20)

# Run the GUI loop
window.mainloop()
