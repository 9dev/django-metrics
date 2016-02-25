import importlib
from inspect import isclass

from django.conf import settings
from django.shortcuts import render

from .metrics import ValueMetric


metrics = importlib.import_module(settings.METRICS_MODULE)

value_metrics = []


# collect metrics
for name, attr in metrics.__dict__.items():
    if isclass(attr):
        if issubclass(attr, ValueMetric) and attr != ValueMetric:
            value_metrics.append(attr())


def metrics(request):
    context = {'value_metrics': value_metrics}
    return render(request, 'metrics/metrics.html', context)
