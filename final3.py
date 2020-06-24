class Point:

    __x = 0
    __y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, b):
        return Point(self.x+b.x, self.y+b.y)
    
    def distance(self, b):
        dis = ((self.x - b.x)**2 + (self.y - b.y)**2)**0.5
        return dis
    

a = Point(1,1)
b = Point(2,2)
print(a.distance(b))
c = a+b
print(c.x,',', c.y)
