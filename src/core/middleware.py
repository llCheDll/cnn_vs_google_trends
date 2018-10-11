import feedparser
from rss_agregator.models import Article
from rss_agregator.trends import get_trends
from core.constants import LINK


class RssMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        feed = feedparser.parse(LINK)
        links = feed.feed['links'][3:]
        trends = get_trends()
        
        for link in links:
            feed = feedparser.parse(link['href'])
            for article in feed['entries']:
                for trend in trends:
                    if trend in article['title'].lower():
                        pass
                    
        response = self.get_response(request)

        
        # Code to be executed for each request/response after
        # the view is called.

        return response
        

        