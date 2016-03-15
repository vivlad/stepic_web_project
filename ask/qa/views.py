from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
def test(request, *args, **kwargs):
    return HttpResponse('OKKK')

def handler404(request):
    return HttpResponse(status=404)