planet_dict = {'수성':91700000,
               '금성':41400000,
               '화성':78400000,
               '목성':628700000,
               '토성':1277400000,
               '천왕성':2750400000,
               '해왕성':4347400000}

name = input("행성 이름 :")
speed = int(input("이동 속도(km/h) : "))
distance = planet_dict[name]

time = distance / speed

year = int(time) // (365*24)
month = int(time-(year*365*24))//(30*24)
day = int(time-(year*365*24)-(30*24*month))//24
hour = int(time - (year*365*24)-(month*30*24)-(day*24))

print("이동 시간 : 약 ",time,"시간")
print("이동 시간 : 약",year,"년",month,"월",day,"일",hour,"시간")
