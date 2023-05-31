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
        moves.side_effect = [(1, 1), (0, 0)]

        self.game.player_movement()

        expected_one = [['', '', ''], ['', 'X', ''], ['', '', '']]
        self.assertEqual(expected_one, self.game.grid)

        self.game.player_movement()

        expected_two = [['O', '', ''], ['', 'X', ''], ['', '', '']]
        self.assertEqual(expected_two, self.game.grid)
