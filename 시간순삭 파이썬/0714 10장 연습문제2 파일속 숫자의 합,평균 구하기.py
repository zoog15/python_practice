infile = open("D:\\pt\data.txt","r",encoding="UTF8")
outfile = open("D:\\pt\output.txt","w",encoding="UTF8")

s = 0 #sum
count = 0 #평균을 구하기위한 카운

for line in infile :
    num = float(line.rstrip()) #data 파일에서 한줄씩 num에 저
    s+=num
    count+=1

outfile.write("합계 :"+str(s) + "\n")
outfile.write("평균 :"+str(s/count))

infile.close()
outfile.close()
