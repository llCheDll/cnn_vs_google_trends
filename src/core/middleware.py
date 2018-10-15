import feedparser
from rss_agregator.models import Article
from rss_agregator.trends import get_trends
from core.links import Links

links = Links()

class RssMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.links = links.get_links()
        # One-time configuration and initialization.

    def __call__(self, request):
        trends = get_trends()
        trend_news = []
        
        for link in self.links:
            feed = feedparser.parse(link)
            for article in feed.entries:
                for trend in trends:
                    # import ipdb
                    # ipdb.set_trace()
                    try:
                        if trend in article.title.lower() or trend in article.summary.lower():
                            if article.title.lower() not in trend_news:
                                trend_news.append(article.title.lower())
                    except AttributeError:
                        pass
        
        response = self.get_response(request)

        
        # Code to be executed for each request/response after
        # the view is called.

        return response
        

        