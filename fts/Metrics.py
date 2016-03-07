from datetime import datetime, timedelta, timezone
from time import sleep

from django.contrib.auth.models import User

from main.models import Article

from ._base import BaseTestCase


class TestMetrics(BaseTestCase):

    def setUp(self):
        super(TestMetrics, self).setUp()

        dt = datetime.utcnow().replace(tzinfo=timezone.utc)
        day = timedelta(days=1)

        User.objects.create(username='a', date_joined=dt)
        User.objects.create(username='b', date_joined=dt-day*2)
        User.objects.create(username='c', date_joined=dt-day*6)
        User.objects.create(username='d', date_joined=dt-day*6)

        Article.objects.bulk_create([Article(), Article(), Article()])
        Article.objects.all().update(created=dt-day*3)

    def test_can_see_single_value_metrics(self):
        # Harriet logs in as an admin.
        self.login_as_admin()

        # She hits metrics dashboard.
        self.get(name='metrics')

        # She sees a metric for total number of articles.
        self.assertIn('total articles: 3', self.get_text())

        # She sees a metric for average number of articles.
        self.assertIn('articles/year:', self.get_text())

    def test_can_see_line_chart_metrics(self):
        # Harriet logs in as an admin.
        self.login_as_admin()

        # She hits metrics dashboard.
        self.get(name='metrics')
        sleep(5)

        # She sees a metric for new sign-ups.
        expected_rows = '[1,0],[2,2],[3,0],[4,0],[5,0],[6,1],[7,0]'
        self.assertIn(expected_rows, self.browser.page_source)

        # She sees correct labels.
        self.assertIn('Day', self.browser.page_source)
        self.assertIn('Sign-ups', self.browser.page_source)

        # She sees a metric for new articles.
        expected_rows = '[1,0],[2,0],[3,0],[4,0],[5,3],[6,0],[7,0]'
        self.assertIn(expected_rows, self.browser.page_source)
        self.assertIn('New articles', self.browser.page_source)
