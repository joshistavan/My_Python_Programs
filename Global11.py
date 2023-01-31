# def function1(n):
#     print(n,'my name is stavan joshi')
# function1('ok,hello bhai')
"""
l=10  #---Global-----
def fun1(a):
    l=5 #local variable
    m=9 #local variable
    print((l+m))
    print(a,'hello stavan')
fun1('hello kana bhai')
print(l)

"""
l=15
def fun2(q):
    #l=2
    m=2
    global l
    l+=15
    print(l+m)
    print('q')
fun2('q')
print(l)












