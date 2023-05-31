def move() -> list:
    row = int(input("Select Row 1-3: ")) - 1
    col = int(input("Select Col 1-3: ")) - 1

    return [row, col]


class Game:

    def __init__(self):
        self.grid = [['', '', ''], ['', '', ''], ['', '', '']]
        self.player_one = "X"
        self.player_two = "O"
        self.count = 0
        self.player_logic = self.count % 2 == 0

    def player_movement(self):
        player = "One" if self.player_logic else "Two"
        moves = move()
        self.grid[moves[0]][moves[1]] = "X" if self.player_logic else "O"
        self.count += 1

    def game(self):
        print("Started Game")
        win = False
        while not win:
            player_turn = "one" if self.count % 2 == 0 else "two"
            print(f"Player {player_turn}s turn")
            self.player_movement()
            if self.count == 8:
                print("It is a draw")
                win = False
