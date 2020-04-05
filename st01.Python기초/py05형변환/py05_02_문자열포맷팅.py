# %s : 문자열 , %d : 10진 정수, %f : 10진 실수
# Thay thế %s : chuỗi, %d : số nguyên, %f : số thực

# 문자열 포매팅 Formating chuỗi
print( "I eat %d apples."%3 ) # 'I eat 3 apples.'

number=10
day="three"
print( "I ate %d apples. I was sick for %s days."%(number, day) )

# 'I ate 10 apples. so I was sick for three days.'
# 정렬과 공백(사용 빈도 높음) Căn lề và khoảng trống, sử dụng nhiều
print( "%10s" % "hi" )        # '        hi'
print( "%-10sjane." % "hi" )  # 'hi        jane.'

# 소수점 표현 Thể hiện số thập phân
print( "%0.4f" % 3.42134234 )  # '3.4213' Chỉ lấy 4 chữ số thập phân
print( "%10.4f" % 3.42134234 ) # '    3.4213' lấy 4 chữ số thập phân và thêm 1 khoảng trống
