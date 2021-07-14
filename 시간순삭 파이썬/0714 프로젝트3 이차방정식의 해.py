import math
import sys

print("ax^2 + bx + c = 0에서 ")
a = float(input("a값 : "))
b = float(input("b값 : "))
c = float(input("c값 : "))

if a == 0 :
    print("a = 0 이므로 이차방정식이 아닙니다. ")
    sys.exit() # 시스템 종료

D = b*b-4*a*c

if D < 0 :
    print("해가 없습니다.")
else :
    x1 = (-b+math.sqrt(D))/(2*a)
    x2 = (-b+math.sqrt(D))/(2*a)
    print("해 : ",x1, ",",x2)
