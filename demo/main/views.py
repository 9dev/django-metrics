from django.http import HttpResponse


def dummy(request):
    return HttpResponse('Go to /metrics')
