from django.http import HttpResponse

from .models import Task


# Create your views here.
def index(request):
    return HttpResponse('hi')


def list_todos(request):
    tasks = Task.objects.all()
    res = '<ul>'
    for t in tasks:
        res += '<li>{}</li>'.format(t)
    res += '</ul>'
    return HttpResponse(res)
