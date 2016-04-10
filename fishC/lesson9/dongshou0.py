print('请输入您的密码：',end=' ')
password = 'zhiqiangyuan'
for i in range(3):
    temp = input()
    if  '*' in temp:
        temp= temp.replace('*','')
    if temp == password:
        print('登陆成功')
    else:
        if i==2:
            print('密码不正确，尝试次数已达到上限，请明天再试！T_T')
        else:
            print('密码不正确，您还有 %d 次尝试机会，请重新输入：'%(2-i),end=' ')
