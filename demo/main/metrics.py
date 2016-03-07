from datetime import datetime, timedelta, timezone

from django.contrib.auth.models import User
from django.db.models import Count

from metrics.metrics import LineChartMetric, ValueMetric

from .models import Article


class AvgArticlesMetric(ValueMetric):
    name = 'articles/year'

    def get_value(self):
        year = timedelta(days=365)
        last_year = datetime.utcnow().replace(tzinfo=timezone.utc) - year
        articles = Article.objects.all().values('created').filter(created__gte=last_year)
        avg = articles.count() / year.total_seconds()
        return avg


class TotalArticlesMetric(ValueMetric):
    name = 'total articles'

    def get_value(self):
        return Article.objects.count()


class NewSignupsMetric(LineChartMetric):
    name = 'new sign-ups'
    xlabel = 'Day'
    ylabel = 'Sign-ups'

    def get_values(self):
        values = []

        now = datetime.utcnow().replace(tzinfo=timezone.utc)
        last7days = now - timedelta(days=7)

        users = User.objects.all().filter(date_joined__gte=last7days)
        signups = users.extra({'day': "date(date_joined)"}).values('day').annotate(signups=Count('pk'))
        data = {row['day']: row['signups'] for row in signups}

        for day, n in ((last7days + timedelta(days=n), n) for n in range(7)):
            day = str(day.date())
            values.append([n+1, data.get(day, 0)])

        return values


class NewArticlesMetric(LineChartMetric):
    name = 'new articles'
    xlabel = 'Day'
    ylabel = 'New articles'

    def get_values(self):
        values = []

        now = datetime.utcnow().replace(tzinfo=timezone.utc)
        last7days = now - timedelta(days=7)

        articles = Article.objects.all().filter(created__gte=last7days)
        publications = articles.extra({'day': "date(created)"}).values('day').annotate(publications=Count('pk'))
        data = {row['day']: row['publications'] for row in publications}

        for day, n in ((last7days + timedelta(days=n), n) for n in range(7)):
            day = str(day.date())
            values.append([n+1, data.get(day, 0)])

        return values
