import re
text = "에러 1122 : 레퍼런스 오류\n 에러 1033 : 아규먼트 오류"
regex = re.compile('에러 1033')
mo = regex.search(text)

if mo != None:
    print(mo.group())
    
import re
text = "문의 사항이 있으면 032-232-6896으로 연락해주세요"
regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = regex.search(text)

if mo != None:
    print(mo.group())