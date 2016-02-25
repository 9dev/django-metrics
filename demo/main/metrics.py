from datetime import datetime

from metrics.metrics import ValueMetric

from .models import Article


class AvgArticlesMetric(ValueMetric):
    name = 'articles/year'

    def get_value(self):
        articles = Article.objects.all().values('created')
        beginning = articles.order_by('created')[0]['created']
        td = datetime.utcnow() - beginning.replace(tzinfo=None)

        avg = articles.count() / (td.total_seconds() / (365*24*60*60))
        return round(avg)


class TotalArticlesMetric(ValueMetric):
    name = 'total articles'

    def get_value(self):
        return Article.objects.count()
