# Nhập vào giá trị 1 và 2
value1 = input("첫번째 과목 점수를 입력하세요: ") 
value2 = input("두번째 과목 점수를 입력하세요: ")

value1 = int(value1) # 문자열 value1을 정수로 변환. 형변환
value2 = int(value2) # 문자열 value1을 정수로 변환. 형변환

sum = value2 + value2  # 합꼐
average = sum / 2      # 평균

print("-" * 10) 
# 점수 평균은 >= 95이면 Very Good을 출력하고 <95이면 Just Good을 출력해요
if average >= 95 :
    print(" Very Good")
else :
    print("Just Good")
print("-" * 10) # ----------