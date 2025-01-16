import random
import math

class DreidelGame:
    def __init__(self):
        self.players = []
        self.player_coins = {}
        self.pot = 0
        self.current_player_index = 0
        self.last_spin = {}

    def initialize_game(self, num_players, initial_coins, initial_pot):
        self.players = [f"Player {i + 1}" for i in range(num_players)]
        self.player_coins = {player: initial_coins for player in self.players}
        self.pot = initial_pot
        self.current_player_index = 0

    def spin_dreidel(self):
        dreidel_sides = ["Nun", "Gimel", "Hey", "Shin"]
        spin_result = random.choice(dreidel_sides)
        self.last_spin[self.players[self.current_player_index]] = spin_result
        return spin_result

    def process_spin(self, spin_result):
        current_player = self.players[self.current_player_index]
        if spin_result == "Nun":
            return f"{current_player} does nothing."
        elif spin_result == "Gimel":
            self.player_coins[current_player] += self.pot
            self.pot = 0
            return f"{current_player} takes the whole pot!"
        elif spin_result == "Hey":
            half_pot = math.ceil(self.pot / 2)
            self.player_coins[current_player] += half_pot
            self.pot -= half_pot
            return f"{current_player} takes half the pot ({half_pot} coins)."
        elif spin_result == "Shin":
            if self.player_coins[current_player] > 0:
                self.player_coins[current_player] -= 1
                self.pot += 1
                return f"{current_player} adds one coin to the pot."
            else:
                return f"{current_player} has no coins to add!"

    def next_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def check_game_over(self):
        active_players = [p for p in self.player_coins if self.player_coins[p] > 0]
        if len(active_players) == 1:
            return active_players[0]
        return None
