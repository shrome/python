from bs4 import BeautifulSoup
import urllib.request 
import requests
from requests import Session

session = requests.Session()
per_session = session.post("https://www.exam-mate.com/reguser/checklogin", 
data={'email':'lawliet5145@gmail.com', 'password':'kAmehAmehA1!'},timeout=None)

NewArr=[]
arr=[]
arrUrl=[]
lenOfArr = []
AlasOfLast = []
url = "https://www.exam-mate.com/topicalpastpapers/?cat=3&subject=16&years=&seasons=&chapter=&paper=&unit=&zone=&level=&offset=0"
ins = url.split("=")
eqn = "="
for s in range(0,10,20):
    ins[-1] = str(s)
    j = eqn.join(ins)
    arrUrl.append(j)
CountStr = 0
counting = 0
count = 0
try:
    while (count < len(arrUrl)):
    #    response = urllib.request.urlopen(arrUrl[count])
        content = BeautifulSoup(session.get(arrUrl[count]).content , "html.parser")
        if (content.find_all('a', class_="qabtn") == None):
            break
        else:
            for anc in content.find_all('a', class_="qabtn"):
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
except:
    print("timeout or connection reset by peer")
    
ques = []
answ = []

for j in range(len(arr)):
    if (j % 2) == 0:
        ques.append(arr[j])
    elif (j % 2) == 1:
        answ.append(arr[j])

quest = []
answe = []
try:
    for i in range(len(ques)):
        for k in range(1,11):
            cont = ques[i].replace('_1.png',"_{k}.png".format(k=k)) if (ques[i].endswith("png")) else ques[i].replace('_1.jpg',"_{k}.jpg".format(k=k)) if (ques[i].endswith("jpg")) else ques[i].replace('_1.jpeg',"_{k}.jpeg".format(k=k))
            if (requests.get(cont).status_code == 200):
                quest.append(cont)
                print(cont)
            cant = answ[i].replace('_1.png',"_{k}.png".format(k=k)) if (answ[i].endswith("png")) else answ[i].replace('_1.jpg',"_{k}.jpg".format(k=k)) if (answ[i].endswith("jpg")) else answ[i].replace('_1.jpeg',"_{k}.jpeg".format(k=k)) if (answ[i].endswith('jpeg')) else answ[i]
            try:
                if (answ[i].endswith("png") or answ[i].endswith("jpg") or answ[i].endswith("jpeg")):
                    if (requests.get(cant).status_code == 200):
                        answe.append(cant)
                        print(cant)
                    else:
                        pass
                        break
                else:
                    answe.append(cant)
                    print(cant)
                    break
            except:
                print("not image error")
except:
    print("connection reset by peer or time out")

f = open("hello.js", "w")
f.write("var ques = {};\n".format(quest))
f.close
f = open("hello.js", "a")
f.write("var answ = {};\n".format(answe))
f.close
f = open("hello.js", "a")
f.write("var title = {};\n".format(NewArr))
f.close

from PIL import Image
from io import BytesIO

outmage = 0
widthImg = []
while (outmage < len(ques)):
    file = BytesIO(urllib.request.urlopen(ques[outmage]).read())
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
        fileans = BytesIO(urllib.request.urlopen(answ[ansmage]).read())
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
