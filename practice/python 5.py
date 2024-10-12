#사용자에게 시험점수를 입력받아
#상/중.하 반으로 분류해주기
#상 - 90점 이상
#중- 70점 이상
#하 - 나머지

size = int(input("시험 점수를 입력해주십시오"))
print(size)

if size >= 90:
    print("상 반")
elif size >= 70:
    print("중 반")
else:
    print("하 반")

if size > 100 or size < 0:
    print("잘못된 정보입니다")


