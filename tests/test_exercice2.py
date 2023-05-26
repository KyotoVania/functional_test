import pytest
import sys
from os.path import abspath, dirname

sys.path.insert(0, abspath(dirname(dirname(__file__))))

# Now you can import the Calculator class
from exercice2 import StringAnalyzer


def test_count_vowels():
    input_string = "Hello, World!"
    analyzer = StringAnalyzer(input_string)
    assert analyzer.count_vowels() == 3

def test_count_consonants():
    input_string = "Hello, World!"
    analyzer = StringAnalyzer(input_string)
    assert analyzer.count_consonants() == 7

def test_count_digits():
    input_string = "Hello123"
    analyzer = StringAnalyzer(input_string)
    assert analyzer.count_digits() == 3

def test_count_words():
    input_string = "Hello, World!"
    analyzer = StringAnalyzer(input_string)
    assert analyzer.count_words() == 2

def test_count_lines():
    input_string = "Hello\nWorld\n"
    analyzer = StringAnalyzer(input_string)
    assert analyzer.count_lines() == 3
