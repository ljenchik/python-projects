import unittest
from main import winner, game


class WinnerTests(unittest.TestCase):
    def test_winner(self):
        name = "Alex"
        self.assertEqual(winner('rock', 'rock', name), f"It's a tie")
        self.assertEqual(winner('rock', 'scissors', name), f'Rock crushes scissors! {name} Wins!')
        self.assertEqual(winner('rock', 'paper', name), f'Paper overs rock! Computer Wins!')




if __name__ == "__main__":
    unittest.main()

