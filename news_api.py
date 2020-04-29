import yaml
from newsapi import NewsApiClient


class NewsApi:
    def __init__(self):
        package = yaml.load(open('package'), Loader=yaml.FullLoader)
        self.api_key = package['api']

    def get_news(self, query):
        news = NewsApiClient(api_key=self.api_key)

        articles = news.get_everything(
            q=query,
            language='en'
        )