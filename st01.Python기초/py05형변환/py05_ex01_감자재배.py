# 감자 재배 Bài toán canh tác khoai tây
# 자급자족: Tự cung tự cấp
#  처음에 20개의 감자가 있었고 매주 감자 10개를 심어서 40개를 수확한다.
#  하루에 감자를 3개씩 먹는다. 1넌 (52주)이 흐르면 감자는 몇개가 될까?

patato = 20
harvestpatato = patato - 10 + 30 * 52
meal = 3*365
sumpatato = harvestpatato - meal
print("감자수는:", sumpatato)
