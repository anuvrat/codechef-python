import sys

def count_letters( word ):
    chars = {}
    for c in word: chars[c] = chars.get( c, 0 ) + 1
    return chars

def main():
    for i in xrange( int( sys.stdin.readline() ) ):
        a, b = sys.stdin.readline().split()
        if count_letters( a ) == count_letters( b ): print "YES"
        else: print "NO"

main()
