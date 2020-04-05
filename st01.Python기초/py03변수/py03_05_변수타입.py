# Variables of diffrent types

#기본형 타입

b = True            #불린
i = 1               #정수 int
f = 0.1             #실수 float 
str1 = "Hello"      #문자열 string
n = None            #None 지정되지 않다

#변수 타입 확인

print(b, type(b))
print(i, type(i))
print(f, type(f))
print(str1, type(str1))
print(n, type(n))

#복합형 타입

l = [0,1,2,0,3]
d = {0: "zero", 1:"one"}
t = (0,1,2)
se1 = set([1,2,3,1,2])
se2 = set("Hello")

#변수 타입 확인

print(l, type(l))   # 중복 가능 배열 liet ke cho phep trung gia tri
print(d, type(d))   # 사전 Tu dien
print(t, type(t))   # 읽기 전용 배열 liet ke dung de doc
print(se1, type(se1))# 중복 불가 배열 Loai bo gia tri trung
print(se2, type(se2)) #중복 불가 배열 Loai bo gia tri trung