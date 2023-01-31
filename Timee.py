import time
initial=time.time()
for i in range(40):
    print('stavan joshi')
print(time.time()-initial)

a=0
initial2=time.time()
while a<=40:
    print('stavan joshi')
    a += 1

print(time.time()-initial2)