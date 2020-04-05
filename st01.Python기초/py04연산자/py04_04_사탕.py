# Cho số tiền và giá của kẹo tính số kẹo tối đa có thể mua được và tiền thừa
myMoney = 5000
candyPrice = 120

# 최대한 살 수 있는 사탕 수
numCandies = myMoney//candyPrice
print(numCandies)

# 최대한 사탕을 구입하고 남은 돈
change = myMoney % candyPrice
print(change)
