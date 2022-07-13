import math
n=int(input('輸入一個正整數n(n>0):'))
ans =0
for i in range(2,round(math.sqrt(n)+1)):
    if n == 2:#因為只有2會出現在i裡面，其他數字根本沒有出現在i裡面
        break
    if n % i == 0:
        ans+=1
    if ans:
        break
if ans :#如果有因數的話那他不是質數
    print('不是質數')
else:
    print('是質數')


