from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.

def render_app(request):
	data = {}
	return render_to_response('app.html', RequestContext(request, data))