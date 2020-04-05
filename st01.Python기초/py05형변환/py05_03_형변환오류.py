# Lỗi chuyển kiểu dữ liệu
try:
    # Dùng lệnh này khi muốn bỏ qua bước này nếu sai kiểu dữ liệu
    #  숫자가 아닌 것을 숫자로 변환 할 때
    int("안녕하세요")
except ValueError:
    print("정수가 아닙니다. 다시 입력하시오. ")

try:
    # 숫자가 아닌 것을 숫자로 변환 할 때
    float("안녕하세요")
except ValueError:
    print("정수가 아닙니다. 다시 입력하시오. ")

try:
    # 소수점이 있는 숫자 형식의 문자열을 int() 함수로 변환 할 때
    int("52.273")
except ValueError:
    print("정수가 아닙니다. 다시 입력하시오. ")


# 숫자가 아닌 것을 정수로 변환하려고 할 때 Khi chuyển chuỗi thành số nguyên
int("안녕하세요")

# 숫자가 아닌 것을 실수로 변환 할 때 Khi chuyển chuỗi thành số thực
float("안녕하세요")

# Khi chuyển số có chữ số thập phân thành kiểu số nguyên
#  소수점이 있는 숫자 형식의 문자열을 int() 함수로 변환하려고 할 때
int("52.273")

# Traceback (most recent call last):
#   File ".\py08_ValueError.py", line 2, in <module>
#     int("안녕하세요")
# ValueError: invalid literal for int() with base 10: "안녕하세요"
