Anagram-Analyzer
=================

Here's my anagram counter. It is roughly consistent with usual descriptions of
anagram counting problems. Specifically, this is a solution for the problem:
"Given a set of words, output the number of words in that set that have at
least one anagram among the other words in the set."

Note that a word is an anagram of itself. Words are also restricted to
alphabetical characters, and our comparisons are case-insensitive.

Some notes on usage:

From the anagram-analyzer directory, you can either:
run the tests (./Test.py), to see that things are working
run the program on your own data (./AnagramAnalyzer.py <wordfile>)
NOTE: You'll need python installed to run the scripts. I've tested them on
python 2.7.3 and 3.3.2 .

If you are running the program on your own data, your word file should contain
one word per line. Words should conform to the following restrictions: only
alphabetical characters, no numbers, whitespace, or punctuation. Words should be
immediately followed by a newline.

For convenience (and fun,) I've included a few word lists in the ./wordlists
directory. The small ones are for my own testing, and the large ones were found
[here](http://www.keithv.com/software/wlist/) and 
[here](http://codehappy.net/wordlist.htm). They show that the algorithm runs 
decently fast on large inputs.  (These files are the reason the directory is
 so huge, but I figured it would be nice to see the code run on them.)

Time complexity:
Roughly speaking, the algorithm is doing the following:
Building a word list (n steps)
Constructing a tuple of letters in each word (n steps)
Looking this tuple up in a dict, and incrementing a value (constant time
increase)
Summing the values in the dict (n steps)
Because the running time of the algorithm is a constant multiple of n, the
algorithm should be O(n). Interestingly, there is a sorting operation happening
when the tuples are constructed (each word's letters are sorted alphabetically.
However, since this word length doesn't depend on the input size n and can't be
described in terms of n, I believe it's fine to exclude that step from the O()
notation. If you were to describe the input as a list of n words, with a total
of m characters, then the running time might be something more like n *
(n/m)log(n/m), because for each term, we're sorting its n/m letters.
