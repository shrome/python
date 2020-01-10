from bs4 import BeautifulSoup
import urllib.request as requests

arr=[]
url = "https://www.exam-mate.com/topicalpastpapers/?cat=3&subject=11&years=&seasons=&paper=&zone=&chapter="
response = requests.urlopen(url)
content = BeautifulSoup(response , "html.parser")
for anc in content.find_all('a', class_="form-control"):
    splitting = anc['onclick'].split(",")[1]
    spli = splitting.translate({ord("'"): None})
    if len(spli) > 2:
        adding = "https://www.exam-mate.com"+spli
        spli = adding.replace(" ","")

    arr.append(spli)

for j in range(len(arr)):
    if (j % 2) == 0:
        print(arr[j])
        requests.urlretrieve(arr[j], "image{}".format(j) + ".png")

for i in range(len(arr)):
    if (i % 2) == 1:
        print(arr[i])
