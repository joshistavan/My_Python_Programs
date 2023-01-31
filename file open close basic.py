#
#             file io basic
#
# r-open file for reading.
# w-open file for writing.
# x- create file if not exists.
# a-add more content to a file.
# t-text mode.
# b-binary mode.
# +-read and write.

#------------------------------------------------
# s=open('myfile.txt')
# a=s.read()
# print(a)
# s.close()
#------------------------------------------------
# f=open('myfile.txt')
# for l in f:
#     print(l,end='')

#-------------------------------------------------
# f=open('myfile.txt')
# print(f.readline())
# print(f.readline())

#------------------------------------------------
# f=open('myfile.txt')
# print(f.readlines())


#file in writing::
# f=open('bhai.txt','w')
# f.write('kana bhai bhole baba na bhagat che')
# f.close()

#------------------------------------------------

# f=open('bhai.txt','a')
# f.write('kana bhai bhole baba na bhagat che\n')
# f.close()

#-------------for file read and write-------------

# f=open('bhai.txt','r+')
# s=f.read()
# print(s)
# s=f.write('jai baba bhole')
# f.close()
#--------------------------------------------------

# f=open('bhai.txt')
# print(f.tell())
# a=f.read()
# print(f.tell())
# print(a)
# print(f.tell())
# f.close()


#seek function is use to check pointer place

f=open('myfile.txt')
# print(f.seek(11))
print(f.read())
print(f.seek(1))

f.close()