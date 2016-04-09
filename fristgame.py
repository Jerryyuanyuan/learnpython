import random
rand_nums = random.randint(0,10)
temp=input('小妹妹，不妨猜一下哥哥手里有几块糖？')
while(temp.isalnum()):
    if temp.isdigit():
        input_num = int(temp)
        break
    else:
        temp = input('输入有误，请重新输入：')

i = 3
while i>0:
    if input_num==rand_nums:
        print('我擦，居然被你猜对了')
        print('糖都给你好了！')
        break
    else:
        if input_num > rand_nums:
            print("大了亲！")
            temp=input('请再次输入：')      
        else:
            print("小了亲！")
            temp=input('请再次输入：')
        while(temp.isalnum()):
            if temp.isdigit():
                input_num = int(temp)
                break
            else:
                temp = input('输入有误，请重新输入：')
        i = i - 1
        if i == 0:
            break
if i==0:
    if input_num == rand_nums:
        print('我擦，居然被你猜对了')
        print('糖都给你好了！')
        print("我没糖吃了！T_T")
    else:
        print("没猜对啊~哈哈！答案是%d" % (input_num))
else:
    print("我没糖吃了！T_T")
