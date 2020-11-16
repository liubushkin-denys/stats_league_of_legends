from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpRequest
from django.template import loader
import os
from dotenv import load_dotenv
from app import api
from django.views import View
import json

load_dotenv()


def index(request):
    template = loader.get_template('app/index.html')
    context = {

    }
    if request.method == 'POST':
        name = str(request.POST['name'])
        region = str(request.POST['region'])
        message = 'No info'
        if name and region:
            try:
                data = api.get_summoner(name, region)
                name = data['name']
                level = data['level']
                avatar = data['avatar']
            except:
                name = 'Summoner not found'
                level = '?'
                avatar = '../static/moai.jpg'
            context = {
                'name': name,
                'level': level,
                'avatar': avatar,
                'region': region,
            }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse(template.render(context, request))
