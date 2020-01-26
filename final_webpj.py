#!/usr/bin/env python
# coding: utf-8
import requests as req,re
from bs4 import BeautifulSoup
item_name=input("Enter the product name:")
snap=req.get("https://www.snapdeal.com/search?keyword="+item_name+"%20pi%204&santizedKeyword=&catId=&categoryId=0&suggested=true&vertical=&noOfResults=20&searchState=&clickSrc=suggested&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy")
flip=req.get("https://www.flipkart.com/search?q="+item_name)
key=input("Enter a keyword:" )
law=re.compile(key,re.I)
sb=snap.content
fb=flip.content
ssoup=BeautifulSoup(sb,"lxml")
fsoup=BeautifulSoup(fb,"lxml")
title=ssoup.find_all('p',{'class':"product-title"})
price=ssoup.find_all('span',{'class':"lfloat product-price"})
avail=ssoup.find_all('span',{'class':"notifyMeSpan"})
favail=fsoup.find_all('div',{'class':"_3O0U0u"})
if fsoup.find('a',{'class':"_2mylT6"})!=None:
    ftitle=fsoup.find_all('a',{'class':"_2mylT6"})
    fprice=fsoup.find_all('div',{'class':"_1vC4OE"})
elif fsoup.find('a',{'class':"_2cLu-l"})!=None:
    ftitle=fsoup.find_all('a',{'class':"_2cLu-l"})
    fprice=fsoup.find_all('div',{'class':"_1vC4OE"})
elif fsoup.find('div',{'class':"_3wU53n"})!=None:
    ftitle=fsoup.find_all('div',{'class':"_3wU53n"})
    fprice=fsoup.find_all('div',{'class':"_1vC4OE _2rQ-NK"})
else:
    print("Sorry,talk to the developer")



    
titlel=[]
pricel=[]
avail1=[]
titlef=[]
pricef=[]
avail2=[]
for i in range(len(title)):
    ssearch=law.search(title[i].get_text())
    if ssearch!=None:
        titlel.append(title[i].get_text())
        pricel.append(price[i].get_text())
        if len(avail)>=i:
            avail1.append("Out of stock")
        else:
            avail1.append("present") 
            
for f in range(len(ftitle)):
    fsearch=law.search(ftitle[f].get_text())
    if fsearch!=None:
        titlef.append(ftitle[f].get_text())
        pricef.append(fprice[f].get_text())
        try:    
            if favail[f].find('div',{'class':"_3aV9Tq"})==None:
                avail2.append("Present")
            else:
                avail2.append("Out of stock")
        except:
            avail2.append("present")
tf=0
pf=0        
tl=0
pl=0
for j in range(len(titlel)):
    if len(titlel[j])>tl:
        tl=len(titlel[j])
    if len(pricel[j])>pl:
        pl=len(pricel[j])
        
for k in range(len(titlef)):
    if len(titlef[k])>tf:
        tf=len(titlef[k])
    if len(pricef[k])>pf:
        pf=len(pricef[k])

if tl!=0:        
    print("SNAPDEAL".center(tl+pl+30,"-"))
    for k in range(len(titlel)):
        print("Name".center(tl+10,"+"),end="")
        print("Price".center(pl+3,"+"),end="")
        print("Availaiblility".center(16,"+"))
        print(titlel[k].ljust(tl+10,"-"),end="")
        print(pricel[k].ljust(pl+3," "),end="")
        print(avail1[k].center(16,"-"))
            
else:
    print("Sorry, No product was found with that name on SNAPDEAL")
    
if tf!=0:        
    print("FLIPKART".center(tf+pf+30,"-"))
    for n in range(len(titlef)):
        print("Name".center(tf+10,"+"),end="")
        print("Price".center(pf+3,"+"),end="")
        print("Availaiblility".center(16,"+"))
        print(titlef[n].ljust(tf+10,"-"),end="")
        print(pricef[n].ljust(pf+3," "),end="")
        print(avail2[n].center(16,"-"))
            
else:
    print("Sorry, No product was found with that name on FlipKart")






