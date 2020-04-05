# 빛의 속도로 프록시마 켄타우리까지 간다면
# 시간이 얼마나 걸리는지 직접 계산해보기로 하자.
# Nếu bạn đến Proxima Centauri với tốc độ ánh sáng, hãy tìm hiểu xem sẽ mất bao lâu.
speed = 300000  # vận tốc ánh sáng là 300.000km/s
distance = 40000000000000  # Quãng đường là 40*10^12
secs = distance/speed  # Thời gian bằng quãng đường / tốc độ

# light_year = secs/(60.0*60.0*24.0*365.0)  # Tính ra thành năm ánh sáng
# print(secs)
# print(light_year)

sec = int(secs)
year = sec//(3600*24*365)
day = (sec - year*3600*24*365)//(3600*24)
hour = (sec - (year*3600*24*365)-(day*24*3600))//3600
phut = (sec - (year*3600*24*365)-(day*24*3600)-(hour*3600))//60
remainder = (sec - (year*3600*24*365)-(day*24*3600) - (hour*3600)) % 60
print(year, "년", day, "일", hour, "시간", phut, "분", remainder, "초 빛의 속도")
