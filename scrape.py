from bs4 import BeautifulSoup
import urllib.request
import requests
from requests import Session

from requests.packages.urllib3 import add_stderr_logger
import urllib
from urllib.error import HTTPError
from urllib.request import urlopen
import re, random, datetime
random.seed(datetime.datetime.now())

add_stderr_logger()

session = requests.Session()
per_session = session.post("https://www.exam-mate.com/reguser/checklogin", 
data={'email':'lawliet5145@gmail.com', 'password':'kAmehAmehA1!'})

chs=['38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58']
i_count=1
""" current_unit = '6(IAL)' """
total_count=0

for x in chs:    
    NewArr=[]
    arr=[]
    arrUrl=[]
    lenOfArr = []
    AlasOfLast = []
    url = "https://www.exam-mate.com/topicalpastpapers/?cat=3&subject=13&years=&seasons=&chapter="+ x +"&paper=&zone=&offset=0"
    ins = url.split("=")
    eqn = "="
    for s in range(0,720,20):
        ins[-1] = str(s)
        j = eqn.join(ins)
        arrUrl.append(j)
    CountStr = 0
    counting = 0
    count = 0
    while (count < len(arrUrl)):
        """ response = urllib.request.urlopen(arrUrl[count]) """
        content = BeautifulSoup(session.get(arrUrl[count]).content , "html.parser") # Use the session to get url
        with open('try.html', "w", encoding="utf-8") as f:
            f.write(str(content.find_all('a', class_="form-control")))
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

    ques = []
    answ = []

    for j in range(len(arr)):
        if (j % 2) == 0:
            ques.append(arr[j])
                

    for i in range(len(arr)):
        if (i % 2) == 1:
            answ.append(arr[i])


quest = []
answe = []
for i in range(len(ques)):
    for k in range(1,11):
        cont = ques[i].replace('_1.png',"_{k}.png".format(k=k)) if (ques[i].endswith("png")) else ques[i].replace('_1.jpg',"_{k}.jpg".format(k=k)) if (ques[i].endswith("jpg")) else ques[i].replace('_1.jpeg',"_{k}.jpeg".format(k=k))
        if (requests.get(cont).status_code == 200):
            quest.append(cont)
            print(cont)
        cant = answ[i].replace('_1.png',"_{k}.png".format(k=k)) if (answ[i].endswith("png")) else answ[i].replace('_1.jpg',"_{k}.jpg".format(k=k)) if (answ[i].endswith("jpg")) else answ[i].replace('_1.jpeg',"_{k}.jpeg".format(k=k))
        if (requests.get(cant).status_code == 200):
            answe.append(cant)
            print(cant)


    f = open("hello.py", "w")
    f.write("ques = {}\n".format(quest))
    f.close
    f = open("hello.py", "a")
    f.write("answ = {}\n".format(answe))
    f.close
    f = open("hello.py", "a")
    f.write("title = {}\n".format(NewArr))
    f.close

    if len(ques) == len(answ) == len(NewArr):
        print('~\n~\n~\n*GREEN* All length are equals to ',len(NewArr))
        total_count = total_count + len(NewArr)
    else:
        print('*RED* Somethings wrong')

    import urllib.request

    #Question
    """ ja = 0
    for i in range(len(ques)):
        filename = NewArr[i+ja].replace('/','-') + '.png'
        fpath = 'png/Biology/Paper'+filename[19]+'/CH'+str(i_count)+'/Question/'
        urllib.request.urlretrieve(ques[i+ja], fpath+filename)
        print(i+1+ja, "-> Saved", fpath+filename) """

    # Answer
    jo = 0
    for i in range(len(answ)):

        if len(answ[i+jo]) <= 40:
            filename = NewArr[i+jo].replace('/','-')
            filename = filename.replace('Q','A')
            fpath = 'png/Biology/Paper'+filename[19]+'/CH'+str(i_count)+'/Answer/'
            f = open(fpath+filename+".txt", "w")
            f.write(answ[i+jo])
            f.close
            print(i+1+jo, "-> Saved", fpath+filename+".txt")
        else:
            filename = NewArr[i+jo].replace('/','-') + '.png'
            filename = filename.replace('Q','A')
            fpath = 'png/Biology/Paper'+filename[19]+'/CH'+str(i_count)+'/Answer/'
            urllib.request.urlretrieve(answ[i+jo], fpath+filename)
            print(i+1+jo, "-> Saved", fpath+filename)
    
    i_count = i_count + 1

#print('{} Questions {} Answers {} Titles'.format(len(ques),len(answ),len(NewArr)))
print('~\n~\n~\nScraped total: ',total_count)

""" from PIL import Image
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
while (ansmage < len(answ)):
    if (len(answ[ansmage]) < 5):
        None
    else:
        fileans = BytesIO(urllib.request.urlopen(answ[ansmage]).read())
        imans = Image.open(fileans)
        widthans , heightans = imans.size
        answidth.append(widthans)
        ansmage += 1

f = open("hello.py", "a")
f.write("widthQues = {}\n".format(widthImg))
f.close
f = open("hello.py", "a")
f.write("widthAnsw = {}\n".format(answidth))
f.close """

ques1R=[];ques2R=[];ques1=[];ques2=[];ques3H=[];ques4H=[];ques3HR=[];ques4HR=[]



""" i = 0
for i in range(len(ques)) :
    if (NewArr[i][19] == "1"):
        if (NewArr[i][20] == "R"):
            ques1R.append(ques[i])
        else:
            ques1.append(ques[i])
    elif (NewArr[i][19] == "2"):
        if (NewArr[i][20] == "R"):
            ques2R.append(ques[i])
        else:
            ques2.append(ques[i])
    elif (NewArr[i][19] == "3"):
        if (NewArr[i][21] == "R"):
            ques3HR.append(ques[i])
        else:
            ques3H.append(ques[i])
    elif (NewArr[i][19] == "4"):
        if (NewArr[i][21] == "R"):
            ques4HR.append(ques[i])
        else:
            ques4H.append(ques[i])
    elif (NewArr[i][19] == "5"):
        ques5.append(ques[i])
    elif (NewArr[i][19] == "6"):
        ques6.append(ques[i])
    elif (NewArr[i][19] == "7"):
        ques7.append(ques[i])
        
print('Paper 1F : ',len(ques1))
print('Paper 1FR: ',len(ques1R))
print('Paper 2F : ',len(ques2))
print('Paper 2FR: ',len(ques2R))
print('Paper 3H : ',len(ques3H))
print('Paper 3HR: ',len(ques3HR))
print('Paper 4H : ',len(ques4H))
print('Paper 4HR: ',len(ques4HR))
print('Total    : ',len(ques1)+len(ques2)+len(ques1R)+len(ques2R))
#+len(ques4)+len(ques5)+len(ques6)+len(ques7) """
