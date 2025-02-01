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

inventory = {'coke':10, 'cider':5, 'milk':5}
price = {'coke':1600, 'cider':1400, "milk":1500}


def print_menu():
    print("menu를 출력합니다.")


def buy_drink():
    print("음료를 선택하고, 구매합니다.")


def switch_mode():
    print("mode를 전환합니다.")


def change_price():
    print("음료의 가격을 변경합니다.")


def add_drink():
    print("음료를 추가합니다.")


def register_drink():
    print("음료를 등록합니다.")


def delete_drink():
    print("음료를 삭제합니다.")


def extract_drink():
    print("음료를 제거합니다.")
   