class News(object):
    def __init__(self, publisher, section, source, title, language,link=None, text=None, mediaUrl=None, timestamp=None):
        self.publisher = publisher
        self.section = section
        self.source = source
        self.title = title
        self.language = language
        self.link = link
        self.text = text
        self.mediaUrl = mediaUrl
        self.timestamp = timestamp
