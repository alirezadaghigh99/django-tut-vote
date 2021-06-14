from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def index_vote(request, *args, **kwargs):
    return HttpResponse("hello")