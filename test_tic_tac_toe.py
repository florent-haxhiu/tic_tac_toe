from unittest import TestCase
from unittest.mock import Mock, patch, PropertyMock, DEFAULT

from tic_tac_toe import Game, move


class TestTicTacToe(TestCase):

    def setUp(self) -> None:
        self.move = move
        self.move = Mock()
        self.player = move
        self.game = Game()

    def test_if_the_Game_class_is_initialized_properly(self):
        expected = [['', '', ''], ['', '', ''], ['', '', '']]
        self.assertEqual(expected, self.game.grid)

    @patch('tic_tac_toe.move')
    def test_if_the_player_one_moves_register_on_grid(self, moves):
        moves.return_value = [1, 1]

        self.game.player_movement()
        expected = [['', '', ''], ['', 'X', ''], ['', '', '']]

        self.assertEqual(expected, self.game.grid)

    @patch('tic_tac_toe.move')
    def test_if_players_one_and_twos_moves_register_on_grid(self, moves):
        count = 0
        moves.side_effect = [(1, 1), (0, 0)]
        expected_one = [['', '', ''], ['', 'X', ''], ['', '', '']]
        expected_two = [['O', '', ''], ['', 'X', ''], ['', '', '']]
        expected = [expected_one, expected_two]

        while count < 2:
            self.game.player_movement()
            self.assertEqual(expected[count], self.game.grid)
            count += 1

    def test_if_win_logic_for_horizontal_with_predefined_grids(self):
        count = 0
        horizontal_win_first_row = [['X', 'X', 'X'], ['', '', ''], ['', '', '']]
        horizontal_win_second_row = [['', '', ''], ['X', 'X', 'X'], ['', '', '']]
        horizontal_win_third_row = [['', '', ''], ['', '', ''], ['X', 'X', 'X']]

        grids = [horizontal_win_first_row, horizontal_win_second_row, horizontal_win_third_row]

        while count < 3:
            self.game.grid = grids[count]

            expected = True
            actual = self.game.check_for_winner("one")

            self.assertEqual(expected, actual)
            count += 1

    def test_if_win_logic_for_vertical_with_predefined_grids(self):
        count = 0
        vertical_win_first_col = [['X', '', ''], ['X', '', ''], ['X', '', '']]
        vertical_win_second_col = [['', 'X', ''], ['', 'X', ''], ['', 'X', '']]
        vertical_win_third_col = [['', '', 'X'], ['', '', 'X'], ['', '', 'X']]

        grids = [vertical_win_first_col, vertical_win_second_col, vertical_win_third_col]

        while count < 3:
            self.game.grid = grids[count]

            expected = True
            actual = self.game.check_for_winner("one")

            self.assertEqual(expected, actual)
            count += 1

    @patch("tic_tac_toe.move")
    def test_game_if_player_x_wins(self, moves):
        moves.side_effect = [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (2, 2)]

        actual = self.game.game()
        expected = True

        self.assertEqual(expected, actual)
