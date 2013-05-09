'''
Created on Mar 1, 2013

@author: anuvrat
'''

import sys

def compute():
    num = 103993
    den = 33102
    pi = []
    for _ in xrange( 1000001 ):
        pi.append( num / den )
        num = ( num % den ) * 10
    return pi[1:]

def main():
    pi = compute()
    for _ in  xrange( int( sys.stdin.readline() ) ):
        accuracy = int( sys.stdin.readline().strip() )
        if accuracy == 0: print "3"
        else:
            print "3." + "".join( map( str, pi[:accuracy] ) )

main()
