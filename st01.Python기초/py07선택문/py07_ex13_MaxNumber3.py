
x = 1
y = 4
z = 5

# 중첩 if 방식
if x > y:
    # x 와 z 를 비교
    if x > z:
        print(x)
    else:
        print(z)

else:
    # y 와 z 를 비교
    if y > z:
        print(y)
    else:
        print(z)

# 연속 if 방식
if x > y and x > z:
    print(x)
elif y > z:
    print(y)
else:
    print(z)
