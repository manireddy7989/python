# def square(x):
#     if x % 2 == 0:
#         return "it's a even number"
#     else:
#         return "it's an odd number"
# print(square(10))
#
# A = {"this", "that"}
# B = {"that", "other"}
# C = {"other", "this"}
# while "other" in C :
#     if "this" in A:
#         A,B,C=A-B,B-C,C-A
#     if "that" in B:
#         A, B, C = C|A, A|B,B|C
# print(C)
# print(A)
# print(B)
# def f(a,b):
#     if(a==0):
#         return b
#     if(a%2 == 1):
#         return 2*f((a-1)/2,b)
#     # return b+f(a-1,b)
# print(f(15,10))

# class que:
#     def __init__(self):
#         self.queue = []
#     def enqueue(self, item):
#         self.queue.append(item)
#     def dequeue(self):
#         if len(self.queue) == 0:
#             return None
#         return self.queue.pop(0)
#     def is_empty(self):
#         return len(self.queue) == 0
#     def size(self):
#         return len(self.queue)
#     def show(self):
#         return self.queue
# queue = que()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# queue.dequeue()
# queue.show()

class cordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(self,other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    def to_orgin(self):
        self.x = 0
        self.y = 0
        
# c = cordinate(3,4)
# orgin = cordinate(0,0)
# v = cordinate(2,4)

# # print(c.distance(orgin))
# print(cordinate.distance(c,orgin))

class Circle():
    def __init__(self,center,radius):
        if type(center) != cordinate:
            raise ValueError
        if type(radius) != int:
            raise ValueError
        
        self.radius = radius    
        self.center = center
    def is_inside(self,point):
        
        return point.distance(self.center) < self.radius
center = cordinate(2,2)
my_cirlce = Circle(center,5)
p = cordinate(3,3)
print(my_cirlce.is_inside(p))



class Simplefraction(onject):
    def __init__(self,n,d):
        self.n = n
        self.d = d
def times(self,oth):
    top = self.n*oth.n
    bottom = self.n*oth.n
    return top/bottom