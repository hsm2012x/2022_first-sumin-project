import pickle

for i in range(1,51):
    with open("{0}주차 보고서.txt".format(i), "w", encoding="utf8") as reportfile:
        reportfile.write("- {0} 주차 주간 보고 -".format(i))
        reportfile.write("\n부서 : ")
        reportfile.write("\n이름 : ")
        reportfile.write("\n업무요약 : ")