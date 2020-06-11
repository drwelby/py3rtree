from collections import namedtuple
from py3rtree import Rect, RTree

Payload = namedtuple('Payload', 'id object')

class Item():

    __slots__ = ('id', 'object', 'bounds', 'handle')

    def __init__(self, leaf):
        leaf_obj = leaf.leaf_obj()
        self.id = leaf_obj.id
        self.object = leaf_obj.object
        self.bounds = []
        self.handle = leaf

    @property
    def bbox(self):
        return self.bounds 

    def __gt__(self, other):
        return self.id > other.id


class Index():

    def __init__(self):
        self.index = RTree()
    
    def insert(self, id=None, bounds=(), obj=None):
        self.index.insert(Payload(id, obj), Rect(*bounds))

    def intersection(self, bounds=(), objects=False):
        results = self.index.query_rect(Rect(*bounds))
        if objects:
            return (Item(result) for result in results if result.is_leaf())
        else:
            return (result.leaf_obj().id for result in results if result.is_leaf())

    @classmethod
    def Property(cls):
        raise NotImplementedError

class Rtree():

    def __init__(self):
        raise NotImplementedError
