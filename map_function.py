#----
# lis=['4','2','6']
# for i in range(len(lis)):
#     lis[i]=int(lis[i])
# lis[1]=lis[1]+5
# print(lis[1])
# lis=['4','2','7','0']
# for i in range(len(lis)):
#     lis[i]=int(lis[i])
# lis[1]+=10
# print(lis[1])
#-------------map_function-----------
# lis=['4','2','7','0']
# lis=list(map(int,lis))
# lis[1]+=10
# print(lis[1])
# def sq(a):
#     return a*a
# num=[2,3,4,5,6,7,9]
# lis=list(map(sq,num))
# print(lis)

#------------lambda-------------------
# def sq(a):
#     return a*a
# def qu(a):
#     return a*a*a
# fsc=[sq,qu]
# for i in range(10):
#     l=list(map(lambda x:x(i),fsc))
#     print(l)
#------------filter--------------
# num=[1,2,3,4,5,6,7,8,9]
# def num__5(num):
#     return num>5
# l=list(filter(num__5,num))
# print(l)

#========------redus------------------

# l=[1,2,3,4]
# num=0
# for i in l:
#     num=num+i
# print(f'our 1+2+3+4 = is ({num})')
from functools import reduce
l=[1,2,3,4]
num=reduce(lambda x,y:x+y,l)
print(f'our 1+2+3+4 = is ({num})')









































