from bs4 import BeautifulSoup
import urllib.request as requests

NewArr=[]
arr=[]
arrUrl=[]
lenOfArr = []
AlasOfLast = []
url = "https://www.exam-mate.com/topicalpastpapers/?cat=3&subject=11&years=&seasons=&chapter=&paper=1&unit=&zone=&level=&offset=0"
ins = url.split("=")
eqn = "="
for s in range(0,2000,20):
    ins[-1] = str(s)
    j = eqn.join(ins)
    arrUrl.append(j)
CountStr = 0
counting = 0
count = 0
while (count < len(arrUrl)):
    response = requests.urlopen(arrUrl[count])
    content = BeautifulSoup(response , "html.parser")
    if (content.find_all('a', class_="form-control") == None):
        break
    else:
        for anc in content.find_all('a', class_="form-control"):
            splitting = anc['onclick'].split(",")[1]
            spli = splitting.translate({ord("'"): None})
            if len(spli) > 2:
                adding = "https://www.exam-mate.com"+spli
                spli = adding.replace(" ","")
            arr.append(spli)

        for tit in content.find_all("div" , class_="question"):
            for title in tit.find_all("div"):
                AlasOfLast.append(title.string)

        while (CountStr < len(AlasOfLast)):
            if (AlasOfLast[CountStr] == None):
                del AlasOfLast[CountStr]
            CountStr += 1

        while (counting < len(AlasOfLast)):
            if (counting % 2 == 0):
                lenOfArr.append(AlasOfLast[counting])
            counting += 1
            
        count += 1


for n in range(len(lenOfArr)) :
    NewArr.append(lenOfArr[n].strip())

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
f.write("var answ = {};\n".format(answ))
f.close
f = open("hello.js", "a")
f.write("var title = {};\n".format(NewArr))
f.close

from PIL import Image
from io import BytesIO

outmage = 0
widthImg = []
while (outmage < len(ques)):
    file = BytesIO(requests.urlopen(ques[outmage]).read())
    ima = Image.open(file)
    width , height = ima.size
    widthImg.append(width)
    outmage += 1

ansmage = 0
answidth = []
if (len(answ[0]) < 5):
    None
else:
    while (ansmage < len(answ)):
        fileans = BytesIO(requests.urlopen(answ[ansmage]).read())
        imans = Image.open(fileans)
        widthans , heightans = imans.size
        answidth.append(widthans)
        ansmage += 1

f = open("hello.js", "a")
f.write("var widthQues = {};\n".format(widthImg))
f.close
f = open("hello.js", "a")
f.write("var widthAnsw = {};".format(answidth))
f.close