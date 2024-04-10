from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
# Render index.html
    return render( request, 'sociala2_app/index.html')
