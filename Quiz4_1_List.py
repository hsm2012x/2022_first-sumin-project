from random import *
lst = range(1,21) #1부터 20
print(lst)
lst = list(lst)
print(lst)
shuffle(lst)
print("치킨 당첨자 : "+str(lst[0]))
#lst.remove(ckichen)
print("커피 당첨자 : "+str(lst[1:4]))
#형변환이 오히려 불편했다
