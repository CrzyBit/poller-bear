from django.http import HttpResponse
from django.template.loader import render_to_string

def index(request):
  page = render_to_string("homepage.html")
  return HttpResponse(page)