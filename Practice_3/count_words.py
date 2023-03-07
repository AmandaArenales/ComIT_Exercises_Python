"""Count the number of words, separated by one or more spaces, 
from a telegram ending in point. It can be assumed that the user 
enters character by character the telegram or the complete sequence, 
which is more comfortable to propose a solution."""

#import re module for regular expression (regex)
import re

def count_words():
    phrase = input("Please, insert a phrase: ")

#\s - matches any whitespace character (spaces, tabs, line breaks),
#{1,} - matches one or more of the preceding token (in our case two or more \s).

    words = re.split(r'\s{1,}', phrase)
    print(words)
    words_len = len(words)
    print(words_len)
    
count_words()