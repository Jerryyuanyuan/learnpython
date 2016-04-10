##member = ['小甲鱼','黑夜','迷途','怡静','秋舞斜阳']
##member.insert(1,88)
##member.insert(3,90)
##member.insert(5,85)
##member.insert(7,90)
##member.insert(9,88)
##print(member)
member = ['小甲鱼','黑夜','迷途','怡静','秋舞斜阳']
ints = [88,90,85,90,88]
ans = []
for i,k in enumerate(member):
    ans.append(k)
    ans.append(ints[i])

print(ans)
