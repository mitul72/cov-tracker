import requests
from bs4 import BeautifulSoup

url="https://www.mygov.in/covid-19/"
def cases():
    res=requests.get(url)
    soup=BeautifulSoup(res.content,'html5lib')
    a = soup.findAll('span')
    count=soup.select(".icount")
    l=[]
    l2=["Cases Across India","Total Cases ","Discharged ","Deaths"]
    dict={}

    for i in count:
        cases=i.text
        l.append(cases)
    for j in range(0,4):
        dict[l2[j]]=l[j]
    return dict
