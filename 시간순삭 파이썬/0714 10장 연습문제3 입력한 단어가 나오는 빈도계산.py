infile = open("D:\\pt\input.txt","r",encoding="UTF8")

search_word = input("단어 입력 : ")

word_dic = {}

for line in infile :
    line = line.rstrip()
    word_list = line.split()

    for word in word_list :
        word = word.lower() #소문자로 변경
        word = word.strip(',') #콤마 삭제
        word = word.strip('.') #마침표 삭제

        if word in word_dic :
            word_dic[word] += 1

        else :
            word_dic[word] = 1

if search_word in word_dic :
    print(search_word + "빈도 : " + str(word_dic[search_word]))
else :
    print(search_word + "빈도 : 0")

infile.close()
