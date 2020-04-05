# py04_05_사각형둘레와면적.py
# Tìm diện tích hình chữ nhật S = D*R area diện tích, perimeter chu vi
l = input("너비 값을 입력하시오 >> ")  # 문자열 length dài
w = input("높이 값을 입력하시오 >> ")  # 문자열 width rộng

try:
    l = float(l)  # 실수로 형변환
    w = float(w)  # 실수로 형변환
except ValueError:
    pass

area = l * w
perimeter = 2 * (l + w)

print("사각형의 넓이:", area)
print("사각형의 둘레:", perimeter)
