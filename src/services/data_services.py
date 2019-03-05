from data.rss import Item
import feedparser as fp


def add_item(rss_item: fp.FeedParserDict, rss_list_item: dict) -> Item:
    item = Item()
    item.title = rss_item.title.strip()
    item.text = rss_item.description.strip()
    item.language = rss_list_item['language']
    item.publisher = rss_list_item['publisher']
    item.section = rss_list_item['section']
    item.source = rss_list_item['source']
    item.link = rss_item.link
    item.save()

    return item


def find_item(rss_item: fp.FeedParserDict, rss_list_item: dict) -> Item:
    return Item.objects(title=rss_item.title, publisher=rss_list_item['publisher']).first()
