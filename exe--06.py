import random
list=['s','w','g']
l1=random.choice(list)
print(l1)
you=0
com=0
chance=1
while (1):
    inp=input('enter your choice,s,w,g:)')
    if inp=='s' and l1=='w':
        print('bhai you win')
        you+=1
    elif inp=='w' and l1=='g':
        print('bhai you are win')
        you+=1
    elif inp=='g' and l1=='s':
        print('bhai you win')
        you+=1
    elif inp==l1:
        print('the match is tai')
    else:
        print('computer wii win')
        com+=1
    chance+=1
    if chance>=10:
        break
        #print('the game is over')
print(f'you win={you},computer win={com}')
if com>=you:
    print('com in this game you will be win')
elif com==you:
    print('The match will be tie')
else:
    print('bhai in this game you will be win')

























