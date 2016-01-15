from django.shortcuts import render_to_response, redirect
from django.views.generic.detail import DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context
from django.shortcuts import render
from models import *
import json
import os
from urlparse import urlparse
import psycopg2


def index(request):

    return render(request, 'index.html')


def map_test(request):

    return render(request, 'test.html')


def map_test2(request):

    return render(request, 'test_2.html')