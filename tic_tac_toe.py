import pprint


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
        row, col = move()
        player_turn = "X" if self.count % 2 == 0 else "O"
        self.grid[row][col] = player_turn
        self.count += 1

    def game(self):
        print("Started Game")
        while self.still_playing:
            player_turn = "one" if self.count % 2 == 0 else "two"
            self.check_for_winner(player_turn)
            print(f"Player {player_turn}s turn")
            self.print_nice_grid()
            if self.player_movement():
                self.still_playing = False
                print(f"Player {player_turn} won")
                break
            if self.count == 8:
                print("It is a draw")
                self.still_playing = False

    def check_for_winner(self, player_number):
        print(player_number)
        player = "X" if player_number == "one" else "O"
        print(player)
        for i in range(len(self.grid)):
            print("Is this being checked", self.grid[i][0] == player and self.grid[i][1] == player and self.grid[i][2] == player)
            if self.grid[i][0] == player and self.grid[i][1] == player and self.grid[i][2] == player:
                return True
            # Vertical Checking, needs to be refactored. Must be a nicer way than this
            elif self.grid[0][i] == player and self.grid[0][i] == player and self.grid[0][i] == player:
                return True
            elif self.grid[1][i] == player and self.grid[1][i] == player and self.grid[1][i] == player:
                return True
            elif self.grid[2][i] == player and self.grid[2][i] == player and self.grid[2][i] == player:
                return True

    def print_nice_grid(self):
        print('\n'.join(' '.join(map(str, x)) for x in self.grid))

# TODO: Need to work on functionality of the win logic as it doesn't end the game when it detects a winner. Strange

# game = Game()
# game.game()
