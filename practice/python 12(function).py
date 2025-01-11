#def calculate(x):
   # return 3*x + 5

#print(calculate(5))


#print("#######################")


def warm_up():
    print("음료를 데웁니다.")


def add_ice():
    print("얼음을 넣습니다.")


def add_esspresso():
    print("espresso를 넣습니다.")


def add_water():
    print("물을 넣습니다.")


def add_milk():
    print("우유를 넣습니다.")


def add_cocoa():
    print("코코아를 넣습니다")

order = input("메뉴를 주문해주십시오")
print(order)

if order == "핫 아메리카노":
    add_esspresso()
    add_water()
    warm_up()

elif order == "아이스 아메리카노":
    add_esspresso()
    add_water()
    add_ice()