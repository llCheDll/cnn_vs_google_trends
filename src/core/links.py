import feedparser

class Links:
    def __init__(self):
        self.link = 'http://edition.cnn.com/services/rss/'
        self.sub_links = []
        
    def get_links(self):
        feed = feedparser.parse(self.link)
        links = feed.feed['links'][3:]
        
        for link in links:
            self.sub_links.append(link['href'])
        
        return self.sub_links
        