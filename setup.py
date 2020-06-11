#!/usr/bin/env python

from setuptools import setup

setup(
    name = "py3rtree",
    packages = ["py3rtree"],
    version = "0.1",
    description = "2-Dimensional RTree spatial index",
    author = "Marc Pfister",
    author_email = "marc.pfister@maxar.com",
    url="https://github.com/maxar-analytics/py3rtree",
    long_description = """\
Two-dimensional RTree spatial index.


This is a simple pure python implemenation of a 2D RTree. For the
moment, it is insert-only, and aimed at creating indexes to speed
queries over mostly-static datasets.

Originally written by Dan Shoutis (dan@shoutis.org).
see http://code.google.com/p/pyrtree

Resurrected by Marc Pfister, with added Rtree compatibility.

"""
)
