from ._base import BaseTestCase


class TestMetrics(BaseTestCase):

    def setUp(self):
        super(TestMetrics, self).setUp()

        # Harriet logs in as an admin.
        self.login_as_admin()

    def test_can_see_single_value_metric(self):
        # Harriet hits metrics dashboard.
        self.get(name='metrics')

        # She sees a metric for total number of articles.
        self.assertIn('Total articles: 10', self.get_text())

    def test_can_see_multiple_single_value_metrics(self):
        # articles total count, avg articles per day
        self.fail()

    def test_can_see_line_chart_metric(self):
        self.fail()

    def test_can_see_multiple_line_chart_metrics(self):
        # new signups, new articles, active users
        self.fail()
