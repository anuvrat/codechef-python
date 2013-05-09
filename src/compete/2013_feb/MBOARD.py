'''
Created on Feb 25, 2013

@author: anuvrat
'''

import sys

def rowQuery( rows, cols, requests ):
    row_id = int( requests[1] ) - 1
    if rows[row_id] == 0:
        print cols.count( 0 )
    else:
        print 0

def colQuery( rows, cols, requests ):
    col_id = int( requests[1] ) - 1
    if cols[col_id] == 0:
        print rows.count( 0 )
    else:
        print 0

def rowSet( rows, cols, requests ):
    row_id, val = int( requests[1] ) - 1, int( requests[2] )
    rows[row_id] = val

def colSet( rows, cols, requests ):
    col_id, val = int( requests[1] ) - 1, int( requests[2] )
    cols[col_id] = val

opers = {"RowQuery" : rowQuery, "ColQuery" : colQuery, "RowSet" : rowSet, "ColSet" : colSet}

def main():
    size, operations = map( int, sys.stdin.readline().strip().split() )

    rows = [0] * size
    cols = [0] * size
    for _ in xrange( operations ):
        requests = sys.stdin.readline().strip().split()
        operator = str( requests[0] )
        opers[operator]( rows, cols, requests )


main()
