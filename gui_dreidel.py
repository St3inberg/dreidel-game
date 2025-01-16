import random
import math
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Treeview, Progressbar
from PIL import Image, ImageTk
import pygame
from dreidel import DreidelGame  # Import the game logic

game = DreidelGame()

# Initialize pygame mixer for music playback
pygame.mixer.init()
pygame.mixer.music.load("spin_sound.mp3")  # Replace with your music file
pygame.mixer.music.play(-1)  # Play music in a loop

def update_player_table():
    """Update the player table with the current game state."""
    for row in player_table.get_children():
        player_table.delete(row)

    for player, coins in game.player_coins.items():
        last_spin = game.last_spin.get(player, "None")
        player_table.insert("", "end", values=(player, coins, last_spin))

def spin_dreidel_handler():
    """Handle the dreidel spin."""
    # Simulate spinning with a loading bar
    dreidel_label.config(text="Spinning...")
    progress_bar["value"] = 0
    root.update()
    for i in range(1, 101, 10):
        progress_bar["value"] = i
        root.update()
        root.after(50)  # Simulate loading delay

    # Perform the spin
    spin_result = game.spin_dreidel()
    dreidel_label.config(text=f"The dreidel lands on {spin_result} ({'נ' if spin_result == 'Nun' else 'ג' if spin_result == 'Gimel' else 'ה' if spin_result == 'Hey' else 'ש'})!")

    # Process the spin result
    result = game.process_spin(spin_result)
    result_label.config(text=result)

    # Update pot and player table
    pot_label.config(text=f"Pot: {game.pot}")
    update_player_table()

    # Check for game over
    winner = game.check_game_over()
    if winner:
        messagebox.showinfo("Game Over", f"{winner} is the only player left with coins and wins the game!")
        pygame.mixer.music.stop()  # Stop music when the game ends
        root.quit()

    # Move to the next player
    game.next_player()
    player_label.config(text=f"Current Player: {game.players[game.current_player_index]}")

def start_game_handler():
    """Start the dreidel game."""
    num_players = int(player_entry.get())
    initial_coins = int(coins_entry.get())
    initial_pot = int(pot_entry.get())

    game.initialize_game(num_players, initial_coins, initial_pot)

    # Update GUI
    player_label.config(text=f"Current Player: {game.players[game.current_player_index]}")
    pot_label.config(text=f"Pot: {game.pot}")
    update_player_table()
    start_button.config(state=tk.DISABLED)
    spin_button.config(state=tk.NORMAL)

# Initialize the GUI application
root = tk.Tk()
root.title("Dreidel Game")

# Input fields for game setup
tk.Label(root, text="Number of Players:").pack()
player_entry = tk.Entry(root)
player_entry.pack()

tk.Label(root, text="Starting Coins per Player:").pack()
coins_entry = tk.Entry(root)
coins_entry.pack()

tk.Label(root, text="Initial Pot Amount:").pack()
pot_entry = tk.Entry(root)
pot_entry.pack()

# Start button
start_button = tk.Button(root, text="Start Game", command=start_game_handler)
start_button.pack()

# Game display labels
player_label = tk.Label(root, text="Current Player:")
player_label.pack()

dreidel_label = tk.Label(root, text="The dreidel lands on...")
dreidel_label.pack()

# Loading bar for spinning animation
progress_bar = Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress_bar.pack()

result_label = tk.Label(root, text="")
result_label.pack()

pot_label = tk.Label(root, text="Pot:")
pot_label.pack()

# Player table
tk.Label(root, text="Player Scores:").pack()
player_table = Treeview(root, columns=("Player", "Gelt", "Last Spin"), show="headings")
player_table.heading("Player", text="Player")
player_table.heading("Gelt", text="Gelt (Coins)")
player_table.heading("Last Spin", text="Last Spin")
player_table.pack()

# Spin button
spin_button = tk.Button(root, text="Spin Dreidel", command=spin_dreidel_handler, state=tk.DISABLED)
spin_button.pack()

# Run the GUI application
root.mainloop()
