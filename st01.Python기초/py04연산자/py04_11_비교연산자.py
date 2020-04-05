# py04_11_비교연산자.py
# Toán tử so sánh cho ra kêt quả đúng hay sai

print("hello" == "hello")  # True
print("hello" == "Hello")  # False
print(12 == 12.0)  # True
print(12 == "12")  # False


print(True)  # True
print(False)  # False

flag = True
print(flag)  # True

flag = (2 > 3)
print(flag)  # False

print(10 == 100)  # False
print(10 != 100)  # True
print(10 < 100)  # True
print(10 > 100)  # False
print(10 <= 100)  # True
print(10 >= 100)  # False


print("가방" == "가방")  # True
print("가방" != "하마")  # True
print("가방" < "하마")  # True
print("가방" > "하마")  # False


x = 25
print(10 < x < 30)  # True
print(10 < x and x < 30)  # True
print(40 < x < 60)  # False
print(40 < x and x < 60)  # True
