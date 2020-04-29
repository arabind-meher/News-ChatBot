import yaml
from newsapi import NewsApiClient

from sentiment_analysis import AnalyzeSentiment

# Getting the 'API' key from yaml file
package = yaml.load(open('package'), Loader=yaml.FullLoader)
api_key = package['api']


class NewsApi:
    # Function to get news from query
    @staticmethod
    def get_news(query):
        news_client = NewsApiClient(api_key=api_key)

        try:
            news_articles = news_client.get_everything(
                q=query,
                language='en'
            )
        except:
            return 'Error'

        articles = news_articles['articles']

        # Dictionary to store news data
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

        # Sentiment Analysis for News
        news = AnalyzeSentiment.analyze_sentiment(news)
        return news
