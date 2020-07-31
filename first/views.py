from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from datetime import datetime

# Create your views here.
def index(request):
    now = datetime.now()
    context = {
        'current_date': now
    }
    return render(request, 'first/index.html', context)


#페이지 두 개 추가하기(페이지 개수만큼 메소드 추가)
def about(request):
    context = {}
    return render(request, 'first/about.html', context)


def product(request):
    context = {}
    return render(request, 'first/product.html', context)


def notice(request):
    context = {}
    return render(request, 'first/notice.html', context)


def qna(request):
    context = {}
    return render(request, 'first/qna.html', context)

