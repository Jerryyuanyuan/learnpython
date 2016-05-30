import random
print("----------------------游戏游戏游戏-----------------")
d = random.randint(1,10)
i = 0
c = input("请输入你猜的数字：")
while True:
    ans = int(c)
    if  ans > d:
        print("值大了")
    elif ans<d:
        print("值小了")
    else:
        print("对了")
        print("猜对了也没有奖励！略略略")
        break
    i=i+1
    c = input("请再次输入你猜的数字：")
print("游戏结束")
