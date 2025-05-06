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
def f(a,b):
    if(a==0):
        return b
    if(a%2 == 1):
        return 2*f((a-1)/2,b)
    # return b+f(a-1,b)
print(f(15,10))