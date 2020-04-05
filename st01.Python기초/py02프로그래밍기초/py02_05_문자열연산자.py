# Toán tử trong python dùng được cho cả chuỗi và số
a = 10
b = 3

#  Phép cộng hoặc kết hợp (결합 연산자)
print("안냥하세요" + " 만나서 반가워요")
print(a + b)

#  Phép trừ 
print(a - b)

# Phép nhân hoặc lặp lại (반복 연산자)
print("반복" * 3)
print (a * b)

#  Phép chia 
print(a/b)

#  Lấy thương của phép chia 
print(a//b)

#  Lấy số dư của phép chia
print(a%b)

#  Lũy thừa. a lũy thừa b
print(a**b)

# 인치 연산자 , toán tử bằng trong chuỗi, chuỗi giống nhau thì cho kết quả đúng mà khác thì sai
print("문자 일치 연산자>>>") #True
print("안녕" == "안녕") #True
print("안녕" == "하이") #False

# 선택 연산자 toán tử lựa chọn 
# Chọn kí tự nào đó trong một chuỗi và chuỗi được đánh số từ 0
# Chọn tiến thì số dương chọn lùi thì số âm 
print("Chọn tiến: ","0123456"[2],"0123456"[4])
print("Chọn lùi: ", "0123456"[-1],"0123456"[-4],"0123456"[-6])

#범위 선택 연산자 toán tử lựa chọn phạm vi sẽ in
print(r"In từ vị trí 0 đến trước vị trí 4 [0:4]:", "0123456"[0:4])

# Lược bỏ phần chữ ở một đầu ## Chưa rõ chỗ naySS
print("Lược bỏ những số trước số thứ 3", "0123456"[3:])
print("Lược bỏ những số sau số thứ 3", "0123456"[:3])