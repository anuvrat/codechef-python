'''
Created on Feb 7, 2013

@author: anuvrat
'''

import sys
import collections

def main():
    for _ in  xrange( int( sys.stdin.readline() ) ):
        jewels = collections.defaultdict( int )
        for j in sys.stdin.readline().strip(): jewels[j] += 1

        cost = 0
        for count in jewels.values(): cost += count / 2 + count % 2
        print cost

main()
