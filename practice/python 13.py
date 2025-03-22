#사용자 모드: 물건 구매
#관리자 모드: 물건 추가, 가격 변동

'''
1. 사용자 모드:
음료의 유무에 따른 재고 안내
해당하는 음료가 없을 시 재입력 요구
어떠한 방식으로 결제하는지 선택(카드, 현금 등)

2. 관리자 모드:
음료의 가격을 정하고 이를 적용
음료를 추가하고 재고 입력
유통기한이 지난 음료 처분
'''
# 각각의 dictionary
inventory = {'coke':10, 'cider':5, 'choco-milk':3}
price = {'coke':800, 'cider':700, 'choco-milk':1000}


mode = "manager"

def print_menu():
    print("menu를 출력합니다.")
    for i in inventory.keys():
        print(i, "가격:", price[i], " 잔여수량:", inventory[i])

def buy_drink():
    print("음료를 선택하고, 구매합니다.")

def switch_mode():
    print("모드를 전환합니다.")
    global mode
    if mode == "manager":
        mode = "user"
    else:
        mode = "manager"

def manager_login():
    print("관리자 모드에 진입합니다.")

def print_function():
    print("관리자가 사용가능한 기능을 출력합니다.")
    print("1. 음료를 등록하기")
    print("2. 음료를 추가하기")
    print("3. 음료를 빼기")
    print("4. 음료를 삭제하기")
    print("5. 사용자 모드로 전환")

def change_price():
    print("음료의 가격을 변경합니다.")

def add_drink():
    print("음료를 추가합니다.")

def register_drink():
    print("음료를 등록합니다.")

def delete_drink():
    print("음료를 삭제합니다.")

def extract_drink():
    print("음료를 뺍니다.")

while True:
    if mode == "manager":
        manager_login()
        user_input =int(input("메뉴를 선택하세요"))

        if user_input == 1:
            register_drink()
        elif user_input == 2:
            add_drink()
        elif user_input == 3:
            extract_drink()
        elif user_input == 4:
            change_price()
            print("어떤 음료를 고르시겠습니까?")
            if user_input == 'coke':
                print("가격을 얼마나 변동시키시겠습니까?")
                price= int(input)


        elif user_input == 5:
            switch_mode()

    else:
        print_menu()
        user_input = input("메뉴를 선택하세요")

print_menu()

drink_key = select_drink()

if drink_key != -1:
    buy_drink(drink_key)


def select_drink():
    global inventory

    drink = int(input("메뉴를 선택하세요"))

    if drink == 1:

        drink_key = 'coke'

    # inventory.update({'coke': inventory['coke'] + 1})

    elif drink == 2:

        inventory['chill sung'] = inventory['chill sung'] + 1

    elif drink == 3:

        inventory['chocolate milk'] = inventory['chocolate milk'] + 1

    elif drink == 4:

        inventory['strewberry milk'] = inventory['strewberry milk'] + 1

    elif drink == 5:

        inventory['banana milk'] = inventory['banana milk'] + 1

    if inventory[drink_key] == 0:

        print("선택한 음료의 수량이 부족합니다.")

        return -1

    else:

        inventory[drink_key] = inventory[drink_key] - 1

        return drink_key


def buy_drink(drink_key: int):
    coin = 0

    while price[drink_key] > coin:
        print("금액을 입력하세요")

        coin = coin + int(input(">>"))

    print(coin - price[drink_key], "원을 반환합니다")
