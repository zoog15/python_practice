import random

infile = open("d:\\pt\hangman.txt","r",encoding = "UTF8")
lines = infile.readlines() #텍스트파일 전체 읽어와서 저장
word = random.choice(lines).rstrip() # 전체중에 한줄 랜덤
solution = list(word)
result = list('_' *len(word)) #list()는 문자열을 받아 리스트로 변환
turns = 10 # 기회는 10번

while turns > 0 :
    guess = input("단어를 추측하세요: ")
    turns -= 1
    i = 0

    for c in word : #guess의 단어가 word안에 있는 단어일시 _ 에서 변
        if c == guess : 
            result[i] = c
        i+= 1

    print(result)
    
    if result == solution :
        print("성공입니다.")
        break

    if turns <= 0:
        print("실패하였습니다.")
        break

infile.close()
