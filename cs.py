import requests
import re
import MySQLdb
import time
import json
db = MySQLdb.connect('localhost','root','ww6822539','mi_db',charset='utf8')
cursor = db.cursor()

start =0
#url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=100&page_start=0'
url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=rank&page_limit=10&page_start={0}'.format(start)

lll = []

for x in range(1):
    txt = requests.get(url)

    txt.endocing = 'utf-8'
    zz = json.loads(txt.text)
    z = zz.values()[0]
    time.sleep(5)
    for i in z:
        name = i['title']    
        rate = float(i['rate'])

        imgurl0 = i['url']
        imgurl1 = re.compile(r'\\')
        imgurl = re.sub(imgurl1,'',imgurl0)
        
        mvurl0 = i['url']
        mvurl1 = re.compile(r'\\')
        mvurl = re.sub(mvurl1,'',mvurl0)
        print rate
        
        try:
            cursor.execute('INSERT INTO douban (name,mvurl,imgurl,rate) values (\'%s\',\'%s\',\'%s\',%f)' % (name,mvurl,imgurl,rate))
            db.commit()
        except Exception as e:
            print e
            db.rollback()
db.close()
