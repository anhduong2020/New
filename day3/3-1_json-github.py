import urllib.request as req
import os.path, random
import json
# tai du lieu xuong va luu voi ten minh muon
# JSON 데이터 내려받기 --- (※1)
url = "https://api.github.com/repositories"
savename = "repo.json"
if not os.path.exists(savename):
    req.urlretrieve(url, savename)

# JSON 파일 분석하기 --- (※2)
# phan tich file bang cach do file
items = json.load(open(savename, "r", encoding="utf-8"))
# 또는
# s = open(savename, "r", encoding="utf-8").read()
# items = json.loads(s)

# print(items)
# exit()
#---------------------------------
# 출력하기 --- (※3)
# chay vong lap theo array
for item in items:
    print(item["name"] + " - " + item["owner"]["login"])

#print('--------------------')
#for item in items:
 #   s = json.dumps(items)
 #  print(s)