#!/usr/bin/python

"""counter.py: A utility for counting occurrences of anagrams in a word list"""

__author__ = "James Magnarelli"
__version__ = "0.1"

import sys
import re

class WordFileParser(object):
  """A class for parsing up the word file"""

  @staticmethod
  def _get_word_and_validate(line):
    """Gets the word on the given line, checking the given line for errors

    Proper lines contain a word followed immediately by a newline character.

    NOTE: Words can only contain alphabetical characters
    
    @param line: A string representing a line to check
    @return: The word on the line if the line is valid, False otherwise"""
    match = re.match(r'(^[A-Za-z]+)\n$', line)
    
    #Check for validity
    return match is not None and match.group(1)
 
  @staticmethod
  def parse_word_file(path):
    """Parse the word file at the given location, handling errors

    @param path: The location of the word file

    @return: A list of words contained in the file"""
    word_list = []

    try:
      with open(path, 'r') as wordfile:
        for num, line in enumerate(wordfile):
          word = WordFileParser._get_word_and_validate(line)
          if word:
            word_list.append(word)
          else:
            sys.exit("ERROR: Invalid text on line {0}".format(num))
    except EnvironmentError: # Failed to open file
      sys.exit("ERROR: Could not open word file at {0}".format(path))

    return word_list


class WordListAnalyzer(object):
  """A Class for analyzing a word lists"""


  @staticmethod
  def _get_word_tuple(word):
    """Convert a word to its character tuple

    A Character tuple is a tuple containing all characters in the word sorted
    in alphabetical order

    @param word: The word to convert

    @return: A tuple containing the given word's letters in lexical order"""

    letter_list = [x for x in word.lower()]
    letter_list.sort()

    return tuple(letter_list)

  @staticmethod
  def count_anagrams(word_list):
    """Count the number of words in the word list with anagrams in the list

    NOTE: A word is an angagram of itself

    @return: The number of words in the word list with anagrams in the list
            This will be a nonzero integer"""

    words_to_tuples = {}
    tuples_to_counts = {}

    # Get each word's tuple - words with the same tuples are anagrams
    for word in word_list:
      word_tuple = WordListAnalyzer._get_word_tuple(word)

      # Map tuples to number of occurrences
      if word_tuple in tuples_to_counts:
        tuples_to_counts[word_tuple] += 1
      else:
        tuples_to_counts[word_tuple] = 0

    # Total it all up
    num_anagrams = 0
    for _, num_occurrences in tuples_to_counts.items():
      # If an anagram has been detected, account for the original occurrence
      if num_occurrences != 0:
        num_anagrams += num_occurrences + 1

    return num_anagrams

def _main():
  if len(sys.argv) != 2:
    print("Usage: {0} <word file>".format(sys.argv[0]))
  word_list = WordFileParser.parse_word_file(sys.argv[1])
  print(WordListAnalyzer.count_anagrams(word_list))
  sys.exit()

if __name__ == '__main__':
  _main()
