from random import *

user = range(1,51)
user = list(user)
count =0
for i in range(1,51):
    user[i-1]=randint(5,50)
    print("{0}번째 손님 (소요시간 : {1}분)".format(i,user[i-1]))
    if 5<=user[i-1]<=15 :
        count += 1
print("총 탑승 승객 : {0}".format(count))