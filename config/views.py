from django.http import HttpResponse
import environ, os

env = environ.Env()
environ.Env.read_env()

def index(request):
    return HttpResponse('Bills Django Server Working...')
