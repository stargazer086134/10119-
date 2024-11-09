#num = -1

#while num > 100 or num <0:
    #num =int(input("수학 성적을 알려주십시오"))

#if num > 80:
   # print("a반입니다")
#elif num > 60:
   # print("b반입니다")
#else:
   # print("c반입니다")

#count = int(input("숫자 하나를 입력해주세요"))

#i=0
#stars = ""
#while i < count:
   # stars = stars + "*"
   # i = i + 1
#print(stars)

#fibonacci = 1
#n = 1
#m = 1

#while fibonacci < 100:
    #print(fibonacci)
    #m = n
    #n = fibonacci
 #   fibonacci = m + n

fibonacci_list = [1,1]
n = 1

while fibonacci_list[n-1] + fibonacci_list[n] < 100:
    fibonacci_list.append(fibonacci_list[n-1] + fibonacci_list[n])
    n = n+1

   print(fibonacci_list)
