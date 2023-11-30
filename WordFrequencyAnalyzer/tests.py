# test_with_unittest.py
import unittest
from main import frequencyAnalyzer
class FrequencyAnalizerTests(unittest.TestCase):
    def test_frequency_analizer(self):
        self.assertEqual(frequencyAnalyzer('text1.txt'), 'and')

# test_with_pytest.py
def test_frequency_analyzer_pass():
    output = frequencyAnalyzer('text1.txt')
    assert output == 'and'


def test_frequency_analyzer_pass():
    output = frequencyAnalyzer('text.txt')
    assert output == 'and,the'

if __name__ == "__main__":
    unittest.main()

