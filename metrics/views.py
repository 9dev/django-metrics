import importlib
from inspect import isclass

from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

from .metrics import LineChartMetric, ValueMetric


metrics = importlib.import_module(settings.METRICS_MODULE)

value_metrics = []
linechart_metrics = []


# collect metrics
for name, attr in metrics.__dict__.items():
    if isclass(attr):
        if issubclass(attr, ValueMetric) and attr != ValueMetric:
            value_metrics.append(attr())
        elif issubclass(attr, LineChartMetric) and attr != LineChartMetric:
            linechart_metrics.append(attr())


@staff_member_required
def metrics(request):
    context = {
        'value_metrics': value_metrics,
        'linechart_metrics': linechart_metrics,
    }
    return render(request, 'metrics/metrics.html', context)
