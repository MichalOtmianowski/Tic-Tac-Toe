import unittest

import tic_tac_toe1


# TODO(lwieczorek) add tests for draw
class TicTacToeStateTest(unittest.TestCase):
    """Tests tic_tac_toe.state."""

    def assert_result(self, board, result):
        self.assertEqual(tic_tac_toe1.state(board), result)

    def test_no_winner(self):
        """No winner."""

        board_a = [
            "XO.",
            ".OX",
            ".X.",
        ]
        board_b = [
            "O..",
            ".X.",
            "..O",
        ]
        self.assert_result(board_a, '.')
        self.assert_result(board_b, '.')

    def test_x_won(self):
        """X won."""

        board = [
            "X..",
            ".X.",
            "..X",
        ]
        self.assert_result(board, 'X')

    def test_o_won(self):
        """O won."""

        board = [
            "..O..",
            "..O..",
            "..O..",
            "..O..",
            "..O..",
        ]
        self.assert_result(board, 'O')

    def test_invalid_dimensions(self):
        """Board has invalid dimensions."""

        board = [
            "XXOO.",
            "...X.",
            "OOOO",
            "...",
            ".....",
        ]
        self.assert_result(board, False)

if __name__ == '__main__':
    unittest.main()
