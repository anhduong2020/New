# 예제로 초 단위의 시간을 받아서 몇 분 몇 초인지를 계산하여 보자.
# Nhập số giây và in ra số giờ phút giây
sec = int(input("입력하세요>>"))
year = sec//(3600*24*365)
day = (sec - year*3600*24*365)//(3600*24)
hour = (sec - (year*3600*24*365)-(day*24*3600))//3600
phut = (sec - (year*3600*24*365)-(day*24*3600)-(hour*3600))//60
remainder = (sec - (year*3600*24*365)-(day*24*3600) - (hour*3600)) % 60
print(year, "년", day, "일", hour, "시간", phut, "분", remainder, "초")
