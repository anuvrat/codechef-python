import sys

def main():
    for _ in xrange( 10 ):
        mods = set()
        for _ in xrange( 10 ):
            mods.add( int( sys.stdin.readline() ) % 42 )
        print len( mods )

main()
