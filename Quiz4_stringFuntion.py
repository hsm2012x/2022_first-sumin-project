
str0 = "http://daum.net"
str1 = str0[7:]
str2=str1[:str1.find(".")]
# print(str0)
# print(str1)
# print(str2)

print(str2[:3]+str(len(str2))+str(str2.count("e"))+"!")
#replace("http://","\0")을 했을때 첫문자가 null이 들어가서 코드가 안깔끔했음
#replace("http://","")로 하면 해결됨
#str.index 와 str.find의 차이?