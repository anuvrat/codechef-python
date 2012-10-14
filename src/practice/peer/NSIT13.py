import sys

def main():
    for i in xrange( 10 ):
        mods = set()
        for j in xrange( 10 ):
            mods.add( int( sys.stdin.readline() ) % 42 )
        print len( mods )

main()
