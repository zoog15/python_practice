import random

def match(c,m) :
    if c == m :
        print("비겼습니다.")
    elif match_table[c] == m : # 컴퓨터가 가위이면 match_table[c] = 보
        print("졌습니다.")
    else :
        print("이겼습니다.")


rps_dic = {1 : '가위', 2 : '바위', 3 : '보'}
match_table = {'가위':'보','바위':'가위','보':'바위'}

computer = rps_dic[random.randint(1,3)] # 컴퓨터에 가위,바위,보중 1개 넣기
mine = input('가위,바위,보 입력 :')
result = match(computer,mine)
print(result)
