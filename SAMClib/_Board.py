import SAMClib
import sys


class Board(object):
    def __init__(self):
        self.nulltile = SAMClib.SmartTile()
        self.nulltile.n = self.nulltile.self
        self.nulltile.ne = self.nulltile.self
        self.nulltile.e = self.nulltile.self
        self.nulltile.se = self.nulltile.self
        self.nulltile.s = self.nulltile.self
        self.nulltile.sw = self.nulltile.self
        self.nulltile.w = self.nulltile.self
        self.nulltile.nw = self.nulltile.self

        self.tiles = [[SAMClib.SmartTile() for col in range(0, 8)] for row in range(0, 8)]

        for row in range(0, 8):
            for col in range(0, 8):
                n1 = (row - 1, col)
                ne1 = (row - 1, col + 1)
                e1 = (row, col + 1)
                se1 = (row + 1, col + 1)
                s1 = (row + 1, col)
                sw1 = (row + 1, col - 1)
                w1 = (row, col - 1)
                nw1 = (row - 1, col - 1)

                n2 = self.tiles[n1[0]][n1[1]] if ((-1 < n1[0] < 8) and (-1 < n1[1] < 8)) else self.nulltile
                ne2 = self.tiles[ne1[0]][ne1[1]] if ((-1 < ne1[0] < 8) and (-1 < ne1[1] < 8)) else self.nulltile
                e2 = self.tiles[e1[0]][e1[1]] if ((-1 < e1[0] < 8) and (-1 < e1[1] < 8)) else self.nulltile
                se2 = self.tiles[se1[0]][se1[1]] if ((-1 < se1[0] < 8) and (-1 < se1[1] < 8)) else self.nulltile
                s2 = self.tiles[s1[0]][s1[1]] if ((-1 < s1[0] < 8) and (-1 < s1[1] < 8)) else self.nulltile
                sw2 = self.tiles[sw1[0]][sw1[1]] if ((-1 < sw1[0] < 8) and (-1 < sw1[1] < 8)) else self.nulltile
                w2 = self.tiles[w1[0]][w1[1]] if ((-1 < w1[0] < 8) and (-1 < w1[1] < 8)) else self.nulltile
                nw2 = self.tiles[nw1[0]][nw1[1]] if ((-1 < nw1[0] < 8) and (-1 < nw1[1] < 8)) else self.nulltile

                self.tiles[row][col].n = n2
                self.tiles[row][col].ne = ne2
                self.tiles[row][col].e = e2
                self.tiles[row][col].se = se2
                self.tiles[row][col].s = s2
                self.tiles[row][col].sw = sw2
                self.tiles[row][col].w = w2
                self.tiles[row][col].nw = nw2

    def __del__(self):
        for line in self.tiles:
            for x in line:
                x.clean()

        self.nulltile.clean()

    def show(self):
        target_tile = self.tiles[0][0]
        sys.stdout.write("" + str(target_tile.nw.get_id()) + "] ")
        sys.stdout.write("" + str(target_tile.n.get_id()) + "] ")
        sys.stdout.write("" + str(target_tile.ne.get_id()) + "] ")
        sys.stdout.write("" + str(target_tile.ne.e.get_id()) + "] ")
        sys.stdout.write("" + str(target_tile.ne.e.e.get_id()) + "] ")
        sys.stdout.write("" + str(target_tile.ne.e.e.e.get_id()) + "] ")
        sys.stdout.write("" + str(target_tile.ne.e.e.e.e.get_id()) + "] ")
        sys.stdout.write("" + str(target_tile.ne.e.e.e.e.e.get_id()) + "] ")
        sys.stdout.write("" + str(target_tile.ne.e.e.e.e.e.e.get_id()) + "] ")
        sys.stdout.write("" + str(target_tile.ne.e.e.e.e.e.e.e.get_id()) + "]")
        sys.stdout.write("\n")
        sys.stdout.flush()
        for x in range(0, 9):
            sys.stdout.write("" + str(target_tile.w.get_id()) + "] ")
            sys.stdout.write("" + str(target_tile.get_id()) + "] ")
            sys.stdout.write("" + str(target_tile.e.get_id()) + "] ")
            sys.stdout.write("" + str(target_tile.e.e.get_id()) + "] ")
            sys.stdout.write("" + str(target_tile.e.e.e.get_id()) + "] ")
            sys.stdout.write("" + str(target_tile.e.e.e.e.get_id()) + "] ")
            sys.stdout.write("" + str(target_tile.e.e.e.e.e.get_id()) + "] ")
            sys.stdout.write("" + str(target_tile.e.e.e.e.e.e.get_id()) + "] ")
            sys.stdout.write("" + str(target_tile.e.e.e.e.e.e.e.get_id()) + "] ")
            sys.stdout.write("" + str(target_tile.e.e.e.e.e.e.e.e.get_id()) + "]")
            sys.stdout.write("\n")
            sys.stdout.flush()
            target_tile = target_tile.s
