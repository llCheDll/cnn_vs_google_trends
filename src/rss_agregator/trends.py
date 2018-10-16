from pytrends.request import TrendReq


def get_trends():
    pytrend = TrendReq()
    # Get Google Hot Trends data
    trends = pytrend.trending_searches()
    trends = trends['title'].tolist()
    return [value for value in trends]
