import _Piece


class Pawn(_Piece.Piece):
    def do_hint(self, parent_tile):
        hint_tiles = []
        if self.team == 0:  # top of board
            hint_tiles.append(parent_tile.s)
            if self.is_init_pos:
                hint_tiles.append(parent_tile.s.s)
        else: # bottom of board
            hint_tiles.append(parent_tile.n)
            if self.is_init_pos:
                hint_tiles.append(parent_tile.n.n)

        for ht in hint_tiles:
            ht.glow = True
        return hint_tiles

