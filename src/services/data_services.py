from time import strftime, gmtime

from data.rss import Item
import feedparser as fp


def add_item(rss_item: fp.FeedParserDict, rss_list_item: dict) -> Item:
    item = Item()
    item.title = rss_item.title.strip()
    if 'media_content' in rss_item:
        item.mediaUrl = rss_item.media_content[0]['url'].replace(" ", "%20")
    item.language = rss_list_item['language']
    item.publisher = rss_list_item['publisher']
    item.section = rss_list_item['section']
    if 'link' in rss_item:
        item.link = rss_item.link
    if 'timestamp' in rss_item:
        item.timestamp = strftime(rss_item.published, gmtime())
    item.save()

    return item


def find_item(rss_item: fp.FeedParserDict, rss_list_item: dict) -> Item:
    return Item.objects(title=rss_item.title, publisher=rss_list_item['publisher']).first()
