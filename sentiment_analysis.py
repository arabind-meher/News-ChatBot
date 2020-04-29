from textblob import TextBlob


class AnalyzeSentiment:
    @staticmethod
    def analyze_sentiment(news):
        for i in range(5):
            text = TextBlob(news[i][0])
            text_hindi = text.translate(to='hi')

            text = TextBlob(news[i][2])
            polarity, subjectivity = text.sentiment

            news[i][1] = text_hindi
            news[i][6] = '%.3f' % polarity
            news[i][7] = '%.3f' % subjectivity

        return news
