
class Piece(object):
    def __init__(self, new_team):
        assert isinstance(new_team, int)
        self.team = new_team
        self.is_init_pos = True

    def do_hint(self, parent_tile):
        return []

    def select(self, parent_tile):
        print "calling select on " + repr(self)
        return self.do_hint(parent_tile)

