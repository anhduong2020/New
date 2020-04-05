# tien hang trainning cho may nhan biet so bang chu viet
# voi du lieu 1000 chu so khac nhau
# va test voi 500 du lieu

from sklearn import model_selection, svm, metrics
# CSV 파일을 읽어 들이고 가공하기 --- (※1)
def load_csv(fname):
    labels = []
    images = []
    with open(fname, "r") as f:
        for line in f:
            cols = line.split(",")
            if len(cols) < 2: continue
            labels.append(int(cols.pop(0)))
            vals = list(map(lambda n: int(n) / 256, cols))
            images.append(vals)
    return {"labels":labels, "images":images}
data = load_csv("./mnist/train.csv")
test = load_csv("./mnist/t10k.csv")
# 학습하기 --- (※2)
clf = svm.SVC()
clf.fit(data["images"], data["labels"])
# 예측하기 --- (※3)
predict = clf.predict(test["images"])
# 결과 확인하기 --- (※4)
ac_score = metrics.accuracy_score(test["labels"], predict)
cl_report = metrics.classification_report(test["labels"], predict)
print("정답률 =", ac_score)
print("리포트 =")
print(cl_report)

# Sau khi hoc cho ket qua xem dung duoc bao nhieu phan tram
# kem theo do la bang bao cao ket qua
