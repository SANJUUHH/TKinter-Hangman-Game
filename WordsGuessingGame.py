import random
import tkinter as tk

words = ['apple', 'banana', 'mango', 'strawberry', 'orange']

word = random.choice(words)

chances = len(word) + 2
guessed_letters = []

root = tk.Tk()
root.title("Hangman")

game_state_label = tk.Label(root, font=("Arial", 24))
game_state_label.pack(pady=20)

guess_entry = tk.Entry(root, font=("Arial", 16))
guess_entry.pack(pady=10)

submit_button = tk.Button(root, text="Guess", command=lambda: handle_guess(guess_entry.get()))
submit_button.pack(pady=10)

def handle_guess(guess):
    global chances
    guess_entry.delete(0, tk.END)

    if guess.lower() in guessed_letters:
        game_state_label.config(text="You already guessed that letter.")
    elif guess.lower() in word:
        guessed_letters.append(guess.lower())
        update_game_state()
        if '_' not in current_state:
            game_state_label.config(text="Congratulations! You've guessed the word: " + word)
            submit_button.config(state=tk.DISABLED)
    else:
        guessed_letters.append(guess.lower())
        chances -= 1
        update_game_state()
        if chances == 0:
            game_state_label.config(text="Sorry, you've run out of chances. The word was: " + word)
            submit_button.config(state=tk.DISABLED)

def update_game_state():
    global current_state
    current_state = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    game_state_label.config(text=' '.join(current_state))

update_game_state()

root.mainloop()

