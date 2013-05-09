'''
Created on Mar 1, 2013

@author: anuvrat
'''

import sys

mapping = {}

def _gen_map( a, b ):
    mapping[b] = a

def generateMapping( language ):
    english = "abcdefghijklmnopqrstuvwxyz"
    map( _gen_map, language, english )
    map( _gen_map, language.upper(), english.upper() )

def main():
    conversations, language = sys.stdin.readline().strip().split()
    generateMapping( language )

    for _ in xrange( int( conversations ) ):
        sentence = sys.stdin.readline().strip()
        english_sentence = []
        for letter in sentence:
            if letter == '_': english_sentence.append( ' ' )
            elif letter in mapping: english_sentence.append( mapping[letter] )
            else: english_sentence.append( letter )
        print "".join( map( str, english_sentence ) )

main()
