import feedparser
import time
import data.mongo_setup as mongo_setup
import logging
import sys

from services.data_services import add_item, find_item
from data.urls import rss_list
from colorama import Fore

logging.basicConfig(stream=sys.stdout, format='%(name)s - %(levelname)s - %(message)s')


def busca_rss():
    for rss_list_item in rss_list:
        feed = feedparser.parse(rss_list_item['url'])
        for feed_entry in feed.entries:
            try:
                if find_item(feed_entry, rss_list_item):
                    logging.info(Fore.YELLOW + f" >>> {feed_entry.title}")
                else:
                    rss_item = add_item(feed_entry, rss_list_item)
                    logging.info(Fore.GREEN + f" +++ {rss_item.title} adicionado com o id {rss_item.id}")
            except Exception as e:
                logging.error(f"{e} - {rss_list_item['publisher']} -> URL: {rss_list_item['url']}")


def main():
    mongo_setup.global_init()
    while True:
        busca_rss()
        time.sleep(60)


if __name__ == '__main__':
    main()
