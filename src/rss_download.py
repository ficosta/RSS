from data.urls import rss_list
from colorama import Fore
import feedparser
import time
import data.mongo_setup as mongo_setup
from services.data_services import add_item, find_item


def busca_rss():
    for rss in rss_list:
        feed = feedparser.parse(rss['url'])
        for feed_entry in feed.entries:
            try:
                if find_item(feed_entry, rss):
                    print(Fore.YELLOW + f" >>> {feed_entry.title}")
                else:
                    rss_item = add_item(feed_entry, rss)
                    print(Fore.GREEN + f" +++ {rss_item.title} adicionado com o id {rss_item.id}")
            except Exception as e:
                print(e)


def main():
    mongo_setup.global_init()
    while True:
        busca_rss()
        time.sleep(30)


if __name__ == '__main__':
    main()
