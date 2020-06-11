import math

class Rect(object):
    """
    A rectangle class that stores: an axis aligned rectangle, and: two
     flags (swapped_x and swapped_y).  (The flags are stored
     implicitly via swaps in the order of minx/y and maxx/y.)
    """

    __slots__ = ("x","y","xx","yy", "swapped_x", "swapped_y")

    def __init__(self, minx,miny,maxx,maxy):
        self.swapped_x = (maxx < minx)
        self.swapped_y = (maxy < miny)
        self.x = minx
        self.y = miny
        self.xx = maxx
        self.yy = maxy

        if self.swapped_x: self.x,self.xx = maxx,minx
        if self.swapped_y: self.y,self.yy = maxy,miny

    @property
    def bounds(self):
        return self.x,self.y,self.xx,self.yy

    def overlap(self, orect):
        return self.intersect(orect).area()

    def write_raw_coords(self, toarray, idx):
        toarray[idx] = self.x
        toarray[idx+1] = self.y
        toarray[idx+2] = self.xx
        toarray[idx+3] = self.yy
        if (self.swapped_x):
            toarray[idx] = self.xx
            toarray[idx+2] = self.x
        if (self.swapped_y):
            toarray[idx + 1] = self.yy
            toarray[idx + 3] = self.y


    def area(self):
        w = self.xx - self.x
        h = self.yy - self.y
        return w * h

    def extent(self):
        x = self.x
        y = self.y
        return (x,y,self.xx-x,self.yy-y)

    def grow(self, amt):
        a = amt * 0.5
        return Rect(self.x-a,self.y-a,self.xx+a,self.yy+a)

    def intersect(self, other):
        if self is NullRect: return NullRect
        if other is NullRect: return NullRect

        nx, ny = max(self.x, other.x),max(self.y, other.y)
        nx2, ny2 = min(self.xx, other.xx),min(self.yy, other.yy)
        w, h = nx2-nx, ny2-ny

        if w < 0 and h < 0:
            return NullRect

        return Rect(nx,ny,nx2,ny2)


    def does_contain(self,o):
        return self.does_containpoint( (o.x,o.y) ) and self.does_containpoint( (o.xx,o.yy) )

    def does_intersect(self,o):
        # return (self.intersect(o).area() > 0)
        r = self.intersect(o)
        return r is not NullRect
        

    def does_containpoint(self,p):
        x,y = p
        return (x >= self.x and x <= self.xx and y >= self.y and y <= self.yy)

    def union(self, other):
        if other is NullRect: return Rect(*self.bounds)
        if self is NullRect: return Rect(*other.bounds)

        nx, ny = min(self.x, other.x), min(self.y, other.y)
        nx2, ny2 = max(self.xx, other.xx), max(self.yy, other.yy)

        return Rect(nx, ny, nx2, ny2)

        
    def union_point(self,o):
        x,y = o
        return self.union(Rect(x,y,x,y))

    def diagonal_sq(self):
        if self is NullRect: return 0
        w = self.xx - self.x
        h = self.yy - self.y
        return w*w + h*h
    
    def diagonal(self):
        return math.sqrt(self.diagonal_sq())

NullRect = Rect(0.0,0.0,0.0,0.0)
NullRect.swapped_x = False
NullRect.swapped_y = False

def union_all(kids):
    cur = NullRect
    for k in kids: cur = cur.union(k.rect)
    assert(False ==  cur.swapped_x)
    return cur
