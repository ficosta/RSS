from urls import rssList
import feedparser
import sqlite3
import time
import rssMQTTNotfier as mqtt
import json
import news

def buscaRSS():
    for rssItem in rssList:
        feed = feedparser.parse(rssItem['url'])
        for entries in feed.entries:
            try:
                newsItem = news.News(publisher=rssItem['publisher'], section=rssItem['section'], source=rssItem['source'], title=entries.title, language=rssItem['language'], text=entries.description)
                streamingRSS(newsItem)
            except Exception as e:
                print(rssItem, e)

def streamingRSS(newsItem):
         mqtt.client.publish("rss/{}".format(newsItem.__dict__['section']), json.dumps(json.dumps(newsItem.__dict__)), qos=0, retain=True)
         print("Publicado: {} - {}".format(newsItem.__dict__['publisher'], newsItem.__dict__['title']))

while True:
    buscaRSS()
    time.sleep(30)
