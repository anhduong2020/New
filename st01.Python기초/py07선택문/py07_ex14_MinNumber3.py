# ex04_03_MaxNumber3.py

x = int( input("첫번째를 입력하세요."))
y = int( input("두번째를 입력하세요."))
z = int( input("세번째를 입력하세요."))

if(  x > y ) :
    if( x > z ) :
        print("입력 받은 수 중에 가장 큰 수는 ", x, "입니다.")
    else :
        print("입력 받은 수 중에 가장 큰 수는 ", z, "입니다.")
else :
    if( y > z ) :
        print("입력 받은 수 중에 가장 큰 수는 ", y, "입니다.")
    else :
        print("입력 받은 수 중에 가장 큰 수는 ", z, "입니다.")



x = int( input("첫번째를 입력하세요."))
y = int( input("두번째를 입력하세요."))
z = int( input("세번째를 입력하세요."))

if(  x > y and  x > z ) :
    print("입력 받은 수 중에 가장 큰 수는 ", x, "입니다.")
elif( y > z ) :
    print("입력 받은 수 중에 가장 큰 수는 ", y, "입니다.")
else :
    print("입력 받은 수 중에 가장 큰 수는 ", z, "입니다.")

