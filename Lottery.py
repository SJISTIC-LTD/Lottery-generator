import random
 
list=[]
def lotto():
    for i in range(10):
        r=random.randint(1,100)
        if r not in list: list.append(r)
 
a = 1
while a < 10:
    lotto()
    print(list)
    a += 1
