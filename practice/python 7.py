num = -1

while num > 100 or num <0:
    num =int(input("수학 성적을 알려주십시오"))

if num > 80:
    print("a반입니다")
elif num > 60:
    print("b반입니다")
else:
    print("c반입니다")