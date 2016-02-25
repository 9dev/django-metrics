from metrics.metrics import ValueMetric

from .models import Article


class TotalArticlesMetric(ValueMetric):
    name = 'Total articles'

    def get_value(self):
        return Article.objects.count()
