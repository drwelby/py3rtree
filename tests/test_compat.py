import unittest
from py3rtree.compat import index

class TestCompat(unittest.TestCase):

    def test_example(self):
        ''' examples from https://toblerity.org/rtree/tutorial.html#creating-an-index '''

        idx = index.Index()
        left, bottom, right, top = (0.0, 0.0, 1.0, 1.0)
        idx.insert(0, (left, bottom, right, top))
        q = list(idx.intersection((1.0, 1.0, 2.0, 2.0)))
        self.assertEqual(q, [0])
        q = list(idx.intersection((1.0000001, 1.0000001, 2.0, 2.0)))
        self.assertEqual(q, [])
        idx.insert(1, (left, bottom, right, top))
        idx.insert(2, bounds=(left, bottom, right, top), obj=42)
        #self.assertEquals(list(idx.nearest((1.0000001, 1.0000001, 2.0, 2.0), 1)), [0, 1])
        q = [n.object for n in idx.intersection((left, bottom, right, top), objects=True)]
        #self.assertEqual(q, [None, None, 42] )
        self.assertEqual(len(q), 3)
        self.assertEqual(set(q), set([None, 42]))
