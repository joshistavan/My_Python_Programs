a=input('enter the name harry Rohan and hammad your choice:)')
if a=='harry':
    b=int(input('Dial 1 for food and 2 for Execise'))
    if b==1:
        s=open('filef1.txt')
        s1=s.read()
        print(s1)
    elif b==2:
        t=open('filef2.txt')
        t1=t.read()
        print(t1)
if a=='rohan':
    b = int(input('please select what can we do'))
    if b==1:
        p=open('filef3.txt')
        p1=p.read()
        print(p1)
    elif b==2:
        m=open('filef4.txt')
        m1=m.read()
        print(m1)
if a=='hammad':
    b = int(input('please select what can we do'))
    if b==1:
        g=open('filef5.txt')
        g1=g.read()
        print(g1)
    elif b==2:
        o=open('filef6.txt')
        o1=o.read()
        print(o1)
else:
        print('you dial in valid sorry bhai')

