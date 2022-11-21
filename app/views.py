from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def wish(request):
    return HttpResponse('Wish you many many returns of the day')