i = 1
while i<=100:
    if i%3==0 and i%7==0:
        print("NavGurukul")
    elif i%3==0:
        print("Nav")
    elif i%7==0:
        print("Gurukul")
    else:
        print(i)
    i = i+1