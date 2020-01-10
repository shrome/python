from bs4 import BeautifulSoup
import urllib.request as requests

arr=[]
arrUrl=[]
url = "https://www.exam-mate.com/topicalpastpapers/?cat=3&subject=11&years=&seasons=&chapter=&paper=1&unit=&zone=&level=&offset=0"
ins = url.split("=")
eqn = "="
for s in range(0,120,20):
    ins[-1] = str(s)
    j = eqn.join(ins)
    arrUrl.append(j)

count = 0
while (count < len(arrUrl)):
    response = requests.urlopen(arrUrl[count])
    content = BeautifulSoup(response , "html.parser")
    for anc in content.find_all('a', class_="form-control"):
        splitting = anc['onclick'].split(",")[1]
        spli = splitting.translate({ord("'"): None})
        if len(spli) > 2:
            adding = "https://www.exam-mate.com"+spli
            spli = adding.replace(" ","")
        arr.append(spli)
    count += 1

ques = []
answ = []

for j in range(len(arr)):
    if (j % 2) == 0:
        ques.append(arr[j])
        

for i in range(len(arr)):
    if (i % 2) == 1:
        answ.append(arr[i])

f = open("hello.js", "w")
f.write("var ques = {};\n".format(ques))
f.close
f = open("hello.js", "a")
f.write("var answ = {};".format(answ))
f.close