from typing import Tuple


def move() -> tuple[int, int]:
    row = int(input("Select Row 1-3: ")) - 1
    col = int(input("Select Col 1-3: ")) - 1

    return row, col


class Game:

    def __init__(self):
        self.grid = [['', '', ''], ['', '', ''], ['', '', '']]
        self.player_one = "X"
        self.player_two = "O"
        self.count = 0

    still_playing = True

    def player_movement(self):
        moves = move()
        row = moves[0]
        col = moves[1]
        player_turn = "X" if self.count % 2 == 0 else "O"
        self.grid[row][col] = player_turn
        self.count += 1

    def game(self):
        print("Started Game")
        print(bool(self.still_playing))
        while self.still_playing:
            player_turn = "one" if self.count % 2 == 0 else "two"
            print(f"Player {player_turn}s turn")
            self.player_movement()
            if self.count == 8:
                print("It is a draw")
                self.still_playing = False
