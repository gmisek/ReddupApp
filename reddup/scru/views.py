from django.template import Context, loader, RequestContext
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, render_to_response, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    return render_to_response('index.html', {}, RequestContext(request))

@csrf_exempt
def create_issue(request):
    if not request.POST:
        return
    desc = request.POST.get('description')
    before_img = request.POST.get('img')
    opener = request.POST.get('opener')
    category = request.POST.get('category')
    location = request.POST.get('location')

    # call create here

    return HttpResponse(json.dumps({'success':True}), content_type='application/json')