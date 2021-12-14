from django.shortcuts import render

# Create your views here.
def mywow(request):
    if request.method == 'GET':
        return render(request, 'mywow.html')
