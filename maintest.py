from collections import namedtuple
import SAMClib
import sys
import gc


b1 = SAMClib.Board()
b1.show()

b1.tiles[1][0]._payload = SAMClib.Pawn(0)
b1.tiles[1][0].select_tile()
b1.show()
print "=" * 20
b1.tiles[1][0].deselect_tile()
b1.show()


#print sys.getrefcount(nulltile)
#print sys.getrefcount(t)



