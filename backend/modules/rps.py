import random

list = ["주먹", "가위", "보"]
result = ["승리", "무승부", "패배"]

def check(me, com):
    if me == com:
        return 1
    elif abs(me - com) == 1:
        if me < com:
            return 0
        else:
            return 2
    elif abs(me - com) == 2:
        if me < com:
            return 2
        else:
            return 0

def get_input(inputs:int):
    while True:
        # print("주먹 : 0, 가위 : 1, 보 : 2")
        # me = int(input("\n0, 1, 2 중 하나의 수를 입력하세요. => "))
        me = inputs
        if me >= 0 and me <= 2:
            return me
        else:
            print("\n0, 1, 2 중 하나의 수를 다시 입력해주세요.")

# 인픗을 하나를 받으면 이겼는지 졌는지 비겼는지를 리턴하는 함수

def play(inputs):
    me = get_input(inputs)
    com = random.randint(0,2)   
    r = check(me, com)
    return f"플레이어는 {list[me]}, 컴퓨터는 {list[com]}, 결과는 {result[r]}입니다."

# com = random.randint(0,2)
# me = get_input()
# r = check(me, com)
# print("\n%s를 선택하셨습니다." % (list[me]))
# print("\n컴퓨터가 %s를 선택하였습니다. 결과는 %s입니다." % (list[com], result[r]))