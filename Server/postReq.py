import requests
from lxml import html
from html.parser import HTMLParser
from bs4 import BeautifulSoup
from lxml import etree
import pandas as pd

 
nosea = 0

class PostRequest:

    def __init__(self, text):
        self.send_request(text)
       
    def send_request(self,text):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'User-Agent': 'Mozilla/5.0',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'www.majento.ru',
            'Origin': 'http://www.majento.ru',
            'Referer': 'http://www.majento.ru/index.php?page=seo-analize/text-semantic/index'
           }

        payload = {
            'page': 'seo-analize/text-semantic/index',
            'url': '',
            'group_fold': '1',
            'query': text,
            'submit': 'Отправить'
                }

        session = requests.Session()
        #session.post('https://admin.example.com/login.php',headers=headers,data=payload)
 
        r = session.post('http://www.majento.ru/index.php?page=seo-analize/text-semantic/index' ,headers=headers, data=payload)
        print(r.text)
        self.determine_all(r.text)

    def determine_all(self, html_string):
        
        global nosea
        tables = pd.read_html(html_string) # Returns list of all tables on page
        #sp500_table = tables[10].text
        #print(sp500_table)
        # table number 9 and 10
        # Без стоп-слов

        withoutStopWords = []
        withStopWords    = []
        speechParts      = []
        dictionary       = []
        
        for ch in tables[9].values:
            
            if 'Тошнота' in ch[0]:
                withoutStopWords.append([ch[0], float(ch[1]) / 100])
                print(ch[0], float(ch[1])/100)
                nosea = float(ch[1])/100
               # yield float(ch[1]) / 100
            else:                
                withoutStopWords.append([ch[0], ch[1]])
                print(ch[0], ch[1])
                
            
       # print(withoutStopWords[0][0] + " " + withoutStopWords[0][1] )
       # print(tables[9].values)
       # for ch in tables[9]:
       #     print(ch)
        # Со стоп-словами
        
        for ch in tables[10].values:        
            withStopWords.append([ch[1],ch[2], float(ch[3])/10,float(ch[4])/10])
            print(str(ch[0]) + " " + str(ch[1]) + " " + str(ch[2])+ " "+ str(float(ch[3])/10)+ " "+ str(float(ch[4])/10))
        print()
        # Части речи
        #print(tables[11].values.T)
        for ch in tables[11].values:
             speechParts.append([ch[1],ch[2], float(ch[3])/10,float(ch[4])/10])
             print(str(ch[0]) +  " " + str(ch[1]) + " " + str(ch[2])+ " "+ str(float(ch[3])/10)+ " "+ str(float(ch[4])/10))
        print()
        # Словарь
        #print(tables[12].values.T)
        for ch in tables[12].values:
            dictionary.append([ch[0], ch[1]])
            print(ch[0], ch[1])
        #for i in tables:
          #  print(i)




#post = PostRequest("одним из важных направлений развития цифровых технологий является их оестествление ")
