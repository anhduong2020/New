
#############################
# 형변환 Chuyển kiểu của biến
#############################

# 문자열을 정수로 변환 Chuyển từ chuỗi thành số nguyên
s = "123"
n = int(s)
print(type(n), n)      # 출력 결과: 124

# 문자열을 실수로 변환 Chuyển chuỗi thành số thực
s = "123.456"
n = float(s) + 1
print(type(n), n)      # 출력 결과: 124.456

# 숫자를 문자열로 변환 : str() 함수 Chuyển số thành chuỗi
n = 123.456
s = str(n) + "ABC"
print(type(s), s)  # 출력 결과: 123.456ABC


#############################
# 형변환과 타입 확인 Chuyển kiểu dữ liệu và xác định type
#############################
output_a = int("52")
output_b = float("52.273")

print(type(output_a), output_a)
print(type(output_b), output_b)

output_a = str(52)
output_b = str(52.273)

print(type(output_a), output_a)
print(type(output_b), output_b)


#############################
# 표준 입력 후 사칙 연산하기 Nhập sau đó tính toán cơ bản
#############################
input_a = input("첫 번째 숫자> ")
input_b = input("두 번째 숫자> ")

input_a = float(input_a)
input_b = float(input_b)

print("덧셈 결과:", input_a + input_b)  # Phép cộng
print("뺄셈 결과:", input_a - input_b)  # Phép trừ
print("곱셈 결과:", input_a * input_b)  # Phép nhân
print("나눗셈 결과:", input_a / input_b)  # Phép chia
