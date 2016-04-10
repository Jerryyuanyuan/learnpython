
##import random

##hezi = []
##daizi = ['红色球','红色球','红色球','黄色球','黄色球','黄色球','绿色球','绿色球','绿色球','绿色球','绿色球','绿色球']

for red in range(0,4):
    for yellow in range(0,4):
        for green in range(0,7):
            if red + yellow + green==8:
                print(red,'\t',yellow,'\t',green)

##for i in range(8):
##    length=len(daizi)
##    index = random.randint(1,length)
##    hezi.append(daizi.pop(index-1))
##print(hezi)
