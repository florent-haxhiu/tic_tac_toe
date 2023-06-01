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
