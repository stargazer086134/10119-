n = 0
m = 0

(n,m) = input("어느 방향으로 이동할까요?")

while n <100 and m <100:
    if str[:2] == "up":
        n = n
        m = m+1
    if str[:4] == "down":
        n = n
        m = m-1
    if str[:4] == "left":
        m = m
        n = n-1
    if str[:5] == "right":
        m = m
        n = n+1



