import sys

class Memoize( object ):
    def __init__( self, f ):
        self.f, self.cache = f, {}

    def __call__( self, *args ):
        if not args in self.cache: self.cache[args] = self.f( *args )
        return self.cache[args]

@Memoize
def reverse( num_str ):
    n_rev = 0
    n = int( num_str )
    while n > 0: n_rev, n = n_rev * 10 + n % 10, n / 10

    return n_rev

def main():
    for _ in xrange( int( sys.stdin.readline() ) ):
        num, steps = int( sys.stdin.readline() ), 0
        while True:
            rev_num = reverse( num )
            if num == rev_num: break
            steps, num = steps + 1, num + rev_num
        print str( steps ) + " " + str( num )

main()
