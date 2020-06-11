# py3rtree

_an updated version of Dan Shoutis' `pyrtree` package_

## About

This package updates Dan Shoutis' `pyrtree` [package](https://code.google.com/archive/p/pyrtree/source/default/source) with these changes:

- A `compat` module that allows drop-in use for much of `rtree`'s API
- Tests, and maintenance
- All Python 3

## Background

The `rtree` [package by Sean Gillies](https://toblerity.org/rtree/) is the standard Python module for implementing RTree spatial indices. Based on the C++ `libspatialindex` library, it is proven and performant.

However, in some cases installing `libspatialindex` is difficult for users, and impossible in some environments. This package aims to offer a drop-in alternative that is pure Python with no library dependencies.

This module is based on the `pyrtree` package originally written by Dan Shoutis and released under a BSD license. 

## Usage

See below for the original instructions from `pyrtree`

For use as a replacement for `rtree` substitute `py3rtree.compat` for `rtree` in your imports:

```python
# from rtree import index
from py3rtree.compat import index
```

This will then work with the `rtree` [example](https://toblerity.org/rtree/tutorial.html):

```pycon
>>> idx = index.Index()
>>> left, bottom, right, top = (0.0, 0.0, 1.0, 1.0)
>>> idx.insert(0, (left, bottom, right, top))
>>> list(idx.intersection((1.0, 1.0, 2.0, 2.0)))
[0]
```

`py3rtree.compat` currently supports:

- `Index()` objects, in-memory only
- `Index.insert()`
- `Index.intersection()`

Not supported (yet):
- `Index().nearest`
- `Rtree()` disc serialization
- point insertion ( as (x,y,x,y) zero-area boxes )


## Original Docs (slightly updated)
------
### pyrtree
An R-Tree implementation

Taken from https://code.google.com/archive/p/pyrtree/source/default/source
(No way to automatically move the versioned source code from code.google.com, so this is copied)

Here's the original project description (https://code.google.com/archive/p/pyrtree/):

### pyrtree
This is a pure python implementation of an RTree spatial index -- with no C library dependencies while retaining decent performance.

I wrote it with the following reasons in mind: * Pure cross-platform python; no C library dependencies. * Access to internal nodes in the tree, allowing for custom traversal strategies. * BSD license

The current version targets in-memory insert-then-query workloads -- updates and persistence are not implemented yet -- and performs quite well at doing so. Besides those limitations, the current version only implements a 2-dimensional index. I'm not sure if this will change: R-tree performance drops quickly as you add dimensions, and I anticipate the largest uses of this library will be by GIS developers, where two-dimensional datasets are commonplace. Planned enhancement: saving and loading the index to disk.

### API
```python
from pyrtree import RTree,Rect

# inserting: 
t = RTree()
t.insert(some_kind_of_object,Rect(min_x,min_y,max_x,max_y))

# querying the whole tree:
# this includes intermediate nodes
point_res = t.query_point( (x,y) )
rect_res = t.query_rect( Rect(x,y,xx,yy) )

# querying only leaf nodes (what you probably want)
# and returning the stored objects
real_point_res = [r.leaf_obj() for r in t.query_point( (x,y) ) if r.is_leaf()]
```

### What is an RTree?
An R-tree is a spatial index over axis-aligned rectangles. (The sides of the rectangles are parallel to the X and Y axes.) They're used heavily in GIS as a way to index geospatial data.

They take the form of trees of rectangles where each node's rectangle contains the rectangle of all its children. The challenge is in deciding how to group rectangles in order to arrive at a well-balanced tree; pyrtree uses k-means clustering to do this. (S. Brakatsoulas, D. Pfoser, and Y. Theodoridis. "Revisiting R-Tree Construction Principles", Advances in Databases and Information Systems 2435 (2002): 17-24)



