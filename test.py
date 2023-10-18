"""
Script:  	test.py
Purpose: 	reverse string while maintaining the original order of words
Developer:	Abdul Hadi
Created:	10/18/2023
"""

import re

def reverse_words_v2(sentense):
    reversed_sentense = ''
    words = sentense.split()
    for i in range(len(words)):
        words[i] = words[i][::-1]
        
    for i in range(len(words)-1):
        reversed_sentense += words[i] + ' '
    reversed_sentense += words[len(words)-1]

    length = len(reversed_sentense)
    return reversed_sentense, length


def reverse_words_v1(sentense):
    words = sentense.split()
    for i in range(len(words)):
        words[i] = words[i][::-1]
        
    reversed_sentense = ' '.join(words)
    length = len(reversed_sentense)
    return reversed_sentense, length

def reverse_words(sentense):
    words = re.findall(r'\b\w+\b',sentense)
    for i in range(len(words)):
        words[i] = words[i][::-1]
        
    reversed_sentense = ' '.join(words)
    length = len(reversed_sentense)

    return reversed_sentense, length

if __name__=="__main__":
    
    reversed_sentense = reverse_words("This is my life")
    print(reversed_sentense)
    
    reversed_sentense = reverse_words_v1("This is my life")
    print(reversed_sentense)

    reversed_sentense = reverse_words_v2("This is my life")
    print(reversed_sentense)
