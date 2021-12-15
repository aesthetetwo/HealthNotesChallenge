from django.shortcuts import render
from django.urls import reverse
from .forms import EditorForm
from django.http import HttpResponseRedirect



# Create your views here.
def mywow(request):
    if request.method == 'GET':
        return render(request, 'mywow.html')

def second_page(request):
      if request.method == 'GET':
        return render(request, 'second_page.html')
