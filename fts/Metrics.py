from ._base import BaseTestCase


class TestMetrics(BaseTestCase):

    def test_can_see_single_value_metric(self):
        # Harriet logs in as an admin.
        # She hits metrics dashboard.
        # She sees a metric for total number of articles.
        # She confirms provided value is correct.
        pass

    def test_can_see_multiple_single_value_metrics(self):
        # articles total count, avg articles per day
        pass

    def test_can_see_line_chart_metric(self):
        pass

    def test_can_see_multiple_line_chart_metrics(self):
        # new signups, new articles, active users
        pass
