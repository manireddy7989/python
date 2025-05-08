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
#     def print(self):
#         print(self.queue)
    
# queue = que()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# queue.dequeue()
# queue.show()
# queue.print()


# class cordinate(object):
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def distance(self,other):
#         x_diff_sq = (self.x - other.x)**2
#         y_diff_sq = (self.y - other.y)**2
#         return (x_diff_sq + y_diff_sq)**0.5
#     def to_orgin(self):
#         self.x = 0
#         self.y = 0
        
# c = cordinate(3,4)
# orgin = cordinate(0,0)
# v = cordinate(2,4)

# # print(c.distance(orgin))
# print(cordinate.distance(c,orgin))

# class Circle():
#     def __init__(self,center,radius):
#         if type(center) != cordinate:
#             raise ValueError
#         if type(radius) != int:
#             raise ValueError        
#         self.radius = radius    
#         self.center = center
#     def is_inside(self,point):       
#         return point.distance(self.center) < self.radius
# center = cordinate(2,2)
# my_cirlce = Circle(center,5)
# p = cordinate(3,3)
# print(my_cirlce.is_inside(p))



# class Simplefraction(object):
#     def __init__(self,n,d):
#         self.n = n
#         self.d = d
#     def times(self,oth):
#         top = self.n*oth.n
#         bottom = self.n*oth.n
#         return top/bottom
#     def plus(self,oth):
#         top = self.n*oth.d + self.d*oth.n
#         bottom = self.d*oth.d
#         return top/bottom
    
# f1 = Simplefraction(3,4)
# f2 = Simplefraction(5,6)
# print(f1)
# print(f1.d)
# print(f1.plus(f2))
# print(f1.times(f2))

# class animal(object):
#     def __init__(self,age):
#         self.age = age
#         self.name = None
#     def __str__(self):
#         return "animal: " + str(self.name)+ ":" + str(self.age)
#     def get_age(self):
#         return self.age
#     def get_name(self):
#         return self.name
#     def set_age(self,newage):
#         self.age = newage
#     def set_name(self,newname = ""):
#         self.name = newname
        
# class cat(animal):
#     def speak(self):
#         print( "meow")
#     def __str__(self):
#         return "cat: " + str(self.name)+ ":" + str(self.age)

# class person(animal):
#     def __init__(self,name,age):
#         animal.__init__(self,age)
#         self.set_name(name)
#         self.friends = []
#     def get_friends(self):
#         return self.friends.copy()
#     def add_friends(self,fname):
#         if fname not in self.friends:
#             self.friends.append(fname)
#     def speak(self):
#         print("hello")
#     def age_diff(self,other):
#         diff = self.set_age - other.age
#         print(abs(diff),"year difference")
#     def __str__(self):
#         return "person: " + str(self.name) + ":" + str(self.age)

# p1 = person("Mani",22)
# p2 = person("Mahesh",26)
# print(p1)
# print(p1.age_diff(p2))
# p1.speak()

# p2 = person("Mahesh", 26)
# p1.speak()

# p1.age_diff(p2)

# def make_pets(d):
#     for k,v in d.items():
#         print(k.get_name()+ ':'+ v.get_name())
# p1 = person("Mani",22)
# p2 = person("Mahesh",26)
# c1 = cat(1)
# c1.set_name("elsa")
# c2 = cat(2)
# c2.set_name("lisa")
# d = {p1:c1,p2:c2}
# make_pets(d)        


# import random
# class student(person):
#     def __init__(self, name, age,major = None):
#         person.__init__(self,name,age)
#         self.major = major
#     def change_major(self,major):
#         self.major = major
#     def speak(self):
#         r = random.random()
#         if r < 0.25:
#             print("I have Homework")
#         elif 0.25 <= r < 0.5:
#             print("I need sleep")
#         elif 0.5 <= r < 0.75:
#             print("I should eat")
#         else:
#             print("i'm still zming ")
# s1 = student('Mani', 22, "AI")
# s2 = student("mahesh",25,"CT")
# print(s1)
# print(s2)
# print(s1.get_name(),"says: ")
# s1.speak()
# print(s2.get_name(),"says: ")
# s2.speak()

     
# c = cat(3)
# c.set_name("cat")
# print(c) 
# c.speak()
# print(c.get_age())
# c.speak()
# def animal_dict(L):
#         d = {}
#         for n in L:
#             if type(n) == int and n >= 0:
#                 d[n] = animal(n)
#         return d
    
# a = animal(3)
# print(a) 
# b = animal(4)
# print(b)
# a.set_name("dog")
# print(a.name)
# print(a.get_name())
# print(a)
# a.set_name()
# print(a)
# L = [2,4,'1',-5,0]
# animals = animal_dict(L)
# for n,a in animals.items():
#     print(f"key {n} with cal {a}")
    
    
# def make_animals(l1,l2):
#     l3 = []
#     for i in range(len(l1)):
#         age = l1[i]
#         name = l2[i]
#         a = animal(age)
#         a.set_name(name)
#         l3.append(a)
#     return l3
# l1 = [2,4,5,6]
# l2 = ["dog","cat","rat","bat"]
# animals = make_animals(l1,l2)   
# for i in animals:
#     print(i)
        