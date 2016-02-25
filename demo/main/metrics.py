from metrics.metrics import ValueMetric


class TotalArticlesMetric(ValueMetric):
    name = 'Total articles'

    def get_value(self):
        return 12
