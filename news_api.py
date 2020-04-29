import yaml
from newsapi import NewsApiClient

from sentiment_analysis import AnalyzeSentiment

package = yaml.load(open('package'), Loader=yaml.FullLoader)
api_key = package['api']


class NewsApi:
    @staticmethod
    def get_news(query):
        news_client = NewsApiClient(api_key=api_key)

        try:
            news_articles = news_client.get_everything(
                q=query,
                language='en'
            )
        except Exception:
            return Exception

        articles = news_articles['articles']

        news = dict()
        for i in range(5):
            add_news = list()
            add_news.append(articles[i]['title'])
            add_news.append('')
            add_news.append(articles[i]['description'])
            add_news.append(articles[i]['author'])
            add_news.append(articles[i]['source']['name'])
            add_news.append(articles[i]['url'])
            add_news.append(0)
            add_news.append(0)

            news[i] = add_news

        news = AnalyzeSentiment.analyze_sentiment(news)
        return news
