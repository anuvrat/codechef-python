import sys

def reverse( num_str ):
    n_rev = 0
    n = int( num_str )
    while n > 0: n_rev, n = n_rev * 10 + n % 10, n / 10

    return n_rev

def main():
    for _ in xrange( int( sys.stdin.readline() ) ):
        a , b = map( reverse, sys.stdin.readline().split() )
        print reverse( a + b )

main()
