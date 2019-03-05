from urls import rssList
import feedparser
import sqlite3
import time

#conn = sqlite3.connect('db/RSS.sqlite')
#cursor=conn.cursor()

def buscaRSS():
    for i in rssList:
        feed = feedparser.parse(i['url'])
        for entries in feed.entries:
            print(type(entries))
            try:
                inserirRSS(i[0], i[1], entries.title)
            except Exception as e:
                print(i, e)

def inserirRSS(publisher, keyword, title):

     cursor.execute("SELECT id FROM RSS WHERE title = ?", [title])
     data=cursor.fetchone()
     if data is None:
         cursor.execute("INSERT INTO RSS (keyword, publisher, title) VALUES (?,?,?)", [keyword,publisher,title])
         conn.commit()
         print("Inserido: {} - {}".format(publisher, title))

while True:
    buscaRSS()
    time.sleep(30)
