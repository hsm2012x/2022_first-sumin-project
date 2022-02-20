def std_weight(height, gender):
    if gender : #1이 남자
        print("키 {0}cm 남자의 표준 체중은 {1:.2f}kg 입니다.".format(height, 0.0001*height * height * 22.00))
    else : #0이 여자
        print("키 {0}cm 여자의 표준 체중은 {1:.2f} 입니다.".format(height,  0.0001*height * height * 21.00))

std_weight(175,1)