from django import template
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def index(request):
  now = datetime.now()
  context = {
    'current_date': now,
  }
  return render(request, 'first/index.html', context)


def select(request):
  chosen = request.GET['number']
  
  context = {
    'number': chosen
  }
  return render(request,'first/select.html', context)


def result(request):
  message = '추첨 결과입니다.'
  return HttpResponse(message)