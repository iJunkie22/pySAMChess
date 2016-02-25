import _Piece


class SmartTile(object):
    tiles_count = 0

    def __init__(self):
        self._n = None
        self._ne = None
        self._e = None
        self._se = None
        self._s = None
        self._sw = None
        self._w = None
        self._nw = None
        self._payload = None
        self.glow = False
        self.hint_queue = []

    @property
    def self(self):
        return self

    @property
    def n(self):
        return self._n

    @property
    def ne(self):
        return self._ne

    @property
    def e(self):
        return self._e

    @property
    def se(self):
        return self._se

    @property
    def s(self):
        return self._s

    @property
    def sw(self):
        return self._sw

    @property
    def w(self):
        return self._w

    @property
    def nw(self):
        return self._nw

    @n.setter
    def n(self, value):
        assert isinstance(value, SmartTile)
        self._n = value

    @ne.setter
    def ne(self, value):
        assert isinstance(value, SmartTile)
        self._ne = value

    @e.setter
    def e(self, value):
        assert isinstance(value, SmartTile)
        self._e = value

    @se.setter
    def se(self, value):
        assert isinstance(value, SmartTile)
        self._se = value

    @s.setter
    def s(self, value):
        assert isinstance(value, SmartTile)
        self._s = value

    @sw.setter
    def sw(self, value):
        assert isinstance(value, SmartTile)
        self._sw = value

    @w.setter
    def w(self, value):
        assert isinstance(value, SmartTile)
        self._w = value

    @nw.setter
    def nw(self, value):
        assert isinstance(value, SmartTile)
        self._nw = value

    @staticmethod
    def __new__(cls, *args, **kwargs):
        obj = super(SmartTile, cls).__new__(cls)
        obj._tile_id = cls.tiles_count
        print("Constructing a tile # " + str(cls.tiles_count) + ".")
        cls.tiles_count += 1
        return obj

    def __del__(self):
        print("Destructing a tile # " + str(self._tile_id) + ".")

    def clean(self):
        del self._n
        del self._ne
        del self._e
        del self._se
        del self._s
        del self._sw
        del self._w
        del self._nw

    def get_id(self):
        if self.glow:
            return "{:>3}".format(str(self._tile_id) + "g")

        else:
            return "{:>3}".format(str(self._tile_id))

    def select_tile(self):
        try:
            assert isinstance(self._payload, _Piece.Piece)
            self.hint_queue = self._payload.select(self)
        except AssertionError:
            print "aborted select"

    def deselect_tile(self):
        for ht in self.hint_queue:
            ht.glow = False



