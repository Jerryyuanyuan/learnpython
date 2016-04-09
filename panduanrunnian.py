year = input('请输入需要判断的年：')

while(year.isalnum()):
    if year.isdigit():
        year = int(year)
        break
    else:
        year = input('请输入正确的年份：')

if year%4==0:
    if year%100!=0:
        print('公元 %d 年是闰年'%(year))
    else:
        if year%400==0:
            print('公元 %d 年是闰年'%(year))
        else:
            print('公元 %d 年不是闰年'%(year))
else:
    print('公元 %d 年不是闰年'%(year))
