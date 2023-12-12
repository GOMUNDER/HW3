from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Court

# Create your views here.
def courts(request):
  mycourts = Court.objects.all().values()
  template = loader.get_template('all_courts.html')
  context = {
    'mycourts': mycourts,
  }
  return HttpResponse(template.render(context, request))

def courtdetails(request, id):
  mycourt = Court.objects.get(id=id)
  template = loader.get_template('court_details.html')
  context = {
    'mycourt': mycourt,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
