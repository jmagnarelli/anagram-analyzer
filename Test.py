#!/usr/bin/python

"""test.py: A set of tests for the anagram counting algorithm"""

__author__ = "James Magnarelli"
__version__ = 0.1

import unittest

from AnagramCounter import WordListAnalyzer, WordFileParser

class Test_WordListAnalyzer(unittest.TestCase):
  """A class for testing the WordListAnalyzer class"""

  def test_gen_tuple(self):
    self.assertEqual(WordListAnalyzer._get_word_tuple("hello"), ('e', 'h', 'l', 'l', 'o'))
    self.assertEqual(WordListAnalyzer._get_word_tuple("HELLO"), ('e', 'h', 'l', 'l', 'o'))
    self.assertEqual(WordListAnalyzer._get_word_tuple("I"), ('i',))
    self.assertEqual(WordListAnalyzer._get_word_tuple("zyxabzzht"), ('a', 'b', 'h', 't', 'x', 'y', 'z', 'z', 'z'))

  def test_count_anagrams(self):
    self.assertEqual(WordListAnalyzer.count_anagrams(["dog"]), 0)
    self.assertEqual(WordListAnalyzer.count_anagrams(["dog", "Aluminum"]), 0)
    self.assertEqual(WordListAnalyzer.count_anagrams(["hat", "tah"]), 2)
    self.assertEqual(WordListAnalyzer.count_anagrams(["stone", "stone"]), 2)
    self.assertEqual(WordListAnalyzer.count_anagrams(["canyon", "CaNyON", "automobile"]), 2)
    self.assertEqual(WordListAnalyzer.count_anagrams(["Act", "cat", "cat", "dog", "dog", "aardvark"]), 5)

class Test_WordFileParser(unittest.TestCase):
  """A class for testing the WordFileParser class"""

  def test_get_word_and_validate(self):
    self.assertEqual(WordFileParser._get_word_and_validate("hello\n"), "hello")
    self.assertEqual(WordFileParser._get_word_and_validate("HELLO\n"), "HELLO")
    self.assertEqual(WordFileParser._get_word_and_validate("I\n"), "I")
    self.assertEqual(WordFileParser._get_word_and_validate("zyxabzzht\n"), "zyxabzzht")
    self.assertEqual(WordFileParser._get_word_and_validate("zyxabzzht"), False)
    self.assertEqual(WordFileParser._get_word_and_validate("\n"), False)
    self.assertEqual(WordFileParser._get_word_and_validate("hey you there\n"), False)
    self.assertEqual(WordFileParser._get_word_and_validate("here-we-go\n"), False)
    self.assertEqual(WordFileParser._get_word_and_validate("number98isthebestplayer\n"), False)

  def test_parse_word_file(self):
    self.assertEqual(WordFileParser.parse_word_file("wordlists/testFile0"),
                    ["pumpernickel"])
    self.assertEqual(WordFileParser.parse_word_file("wordlists/testFile1"),
                    ["roses", "are", "red", "violets", "are", "blue",
                      "roses", "roses", "blue", "blueroses"])
    self.assertEqual(WordFileParser.parse_word_file("wordlists/testFile2"), [])
    self.assertEqual(WordFileParser.parse_word_file("wordlists/testFile3"),
                    ["This", "IS", "a", "file", "of", "somewords", "that",
                      "I", "am", "using", "to", "test", "my", "file",
                      "parsing", "function", "i", "hope", "itworkswell"])

if __name__ == '__main__':
  unittest.main()
