from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.


def index(request):
    try:
     return render(request, "./onlinecourses/index.html")

    except:
       response_data =render_to_string("404.html")
       return HttpResponseNotFound(response_data)
       





