import random
import time
import math
import pygame  # For music playback

def loading_effect():
    """Creates a loading effect to simulate the dreidel spinning with music."""
    spinner = ["[□]", "[▣]", "[■]", "[▣]"]  # Cube visual effect

    # Initialize pygame mixer and load music
    pygame.mixer.init()
    pygame.mixer.music.load("D:\python\spin_sound.mp3")  # Replace with your audio file
    pygame.mixer.music.play(-1)  # Play music in a loop during spinning

    print("Spinning the dreidel...", end=" ")
    for _ in range(8):  # Adjust number of spins as needed
        for frame in spinner:
            print(frame, end="\r", flush=True)
            time.sleep(0.4)  # Slow spin effect

    pygame.mixer.music.stop()  # Stop music after spinning
    print(" " * 20, end="\r")  # Clear the line

def dreidel_game():
    # Initial settings
    players = int(input("Enter the number of players: "))
    initial_coins = int(input("Enter the starting coins for each player: "))
    initial_pot = int(input("Enter the initial amount in the pot: "))

    # Initialize players and pot
    player_coins = {f"Player {i+1}": initial_coins for i in range(players)}
    pot = initial_pot
    dreidel_sides = ["Nun", "Gimel", "Hey", "Shin"]

    print(f"\nStarting game with {players} players and {initial_pot} coins in the pot.")
    print(f"Each player starts with {initial_coins} coins.")
    print("-" * 30)

    while True:  # Infinite loop until the user decides to end
        for player in player_coins:
            if player_coins[player] <= 0:
                continue  # Skip players with no coins

            input(f"{player}, press Enter to spin the dreidel.")
            loading_effect()  # Simulate spinning
            spin = random.choice(dreidel_sides)
            print(f"The dreidel lands on... {spin}!")

            if spin == "Nun":
                print(f"{player} does nothing.")
            elif spin == "Gimel":
                print(f"{player} takes the whole pot!")
                player_coins[player] += pot
                pot = 0
            elif spin == "Hey":
                half_pot = math.ceil(pot / 2)
                print(f"{player} takes half the pot ({half_pot} coins).")
                player_coins[player] += half_pot
                pot -= half_pot
            elif spin == "Shin":
                print(f"{player} adds one coin to the pot.")
                if player_coins[player] > 0:
                    player_coins[player] -= 1
                    pot += 1
                else:
                    print(f"{player} has no coins to add!")

            # Display current status
            print(f"Pot: {pot}, Player Coins: {player_coins}")
            print("-" * 30)

            # Check if any player has won or lost completely
            active_players = [p for p in player_coins if player_coins[p] > 0]
            if len(active_players) == 1:
                print(f"{active_players[0]} is the only player left with coins and wins the game!")
                return

        # Ask if the game should continue
        continue_game = input("Do you want to continue the game? (yes/no): ").strip().lower()
        if continue_game != "yes":
            print("Ending the game...")
            break

    # Determine winner or final status
    print("Game Over!")
    for player, coins in player_coins.items():
        print(f"{player} has {coins} coins.")
    winner = max(player_coins, key=player_coins.get)
    print(f"The winner is {winner}!")

# Run the game
dreidel_game()