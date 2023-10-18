"""
Script:  	test.py
Purpose: 	reverse string while maintaining the original order of words
Developer:	Abdul Hadi
Created:	10/18/2023
"""

import re

def reverse_words(sentence):
    
    words = re.findall(r'\S+|\b\w+\b', sentence)
    
    for i in range(len(words)):
        words[i] = words[i][::-1]
        
    if len(words) > 1:
        reversed_sentence = ' '.join(words)
    else:
        reversed_sentence = words[0] if len(words) == 1 else ""
    
    print(reversed_sentence)
    return reversed_sentence


def test_reverse_words():
    assert reverse_words("Hello World") == "olleH dlroW"
    assert reverse_words("Python is great") == "nohtyP si taerg"
    assert reverse_words("123 456 789") == "321 654 987"
    assert reverse_words("") == ""
    assert reverse_words("SingleWord") == "droWelgniS"
    assert reverse_words("    Spaces    Between    Words    ") == "secapS neewteB sdroW"
    assert reverse_words("    -12-3    21-23-  ") == "3-21- -32-12"


if __name__=="__main__":

    test_reverse_words()
