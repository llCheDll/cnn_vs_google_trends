import feedparser
import re
import threading
import time

from datetime import datetime
from rss_agregator.trends import get_trends
from rss_agregator.links import Links
from rss_agregator.models import Article


class ThreadingFilter(object):
    def __init__(self, interval=60):
        self.interval = interval
        self.links = Links().get_links()

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            trends = get_trends()
            for link in self.links:
                feed = feedparser.parse(link)
                for article in feed.entries:
                    for trend in trends:
                        form = article.title

                        if article.has_key('summary'):
                            form += article.summary

                        form = re.sub(r'[^a-zA-Z\s]', '', form)

                        if trend.lower() in form.lower():
                            if not article.has_key('published'):
                                published = datetime.now().strftime("%d %m %Y %H:%M:%S")
                            else:
                                published = article.published

                            db_article = Article.objects.filter(link=article.link).count()
                            if not db_article:
                                art = Article(
                                    title=article.title,
                                    link=article.link,
                                    created=published,
                                    trend=trend
                                )
                                art.save()

            time.sleep(self.interval)
