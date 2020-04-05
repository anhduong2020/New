
x = 10
y = 20

x = int(input("x 값을 입력하세요>>"))
y = int(input("y 값을 입력하세요>>"))

print("교환 전: ",  x, y)

temp = x
x = y
y = temp

print("교환 후: ",  x, y)
