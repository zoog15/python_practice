contacts = {}

while True :
    name = input("(입력모드)이름을 입력하시오: ")
    if not name : ## 그냥 엔터 쳣을경
        break;
    tel = input("전화번호를 입력하시오: ")
    contacts[name] = tel

while True :
    search = input("(검색모드)이름을 입력하시오. ")
    if search in contacts :
        print(search,"의 전화번호는 ",contacts[search],"입니다.")
    else :
        print("없는 이름입니다.")
        break
