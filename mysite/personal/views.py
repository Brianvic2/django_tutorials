from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'personal/home.html')


def contact(request):
    return render(request, 'personal/basic.html', {'content': ['contact me @.', 'brivicogaga@gmail.com', 'Tel-+254795836827']})
