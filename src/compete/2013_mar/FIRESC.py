'''
Created on Mar 1, 2013

@author: anuvrat
'''

import sys
from types import IntType

def getGroup( group, emp ):
    while type( group[emp] ) is IntType:
        emp = group[emp]

    return emp

def main():
    for _ in  xrange( int( sys.stdin.readline() ) ):
        employees, friendships = map( int, sys.stdin.readline().strip().split() )
        group = {}
        for idx in xrange( employees ):
            group[idx] = [idx]

        for _ in xrange( friendships ):
            friendA, friendB = map( int, sys.stdin.readline().strip().split() )
            grpAIdx = getGroup( group, friendA - 1 )
            grpBIdx = getGroup( group, friendB - 1 )

            if grpAIdx == grpBIdx: continue

            group[grpAIdx].extend( group[grpBIdx] )
            group[grpBIdx] = grpAIdx

            print group

        count_groups = 0
        count_captains = 1
        for grp in group.values():
            if type( grp ) is IntType: continue
            count_groups += 1
            count_captains *= len( grp )

        print count_groups, count_captains

main()
