from .models import Issue
from django.template import Context, loader, RequestContext
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, render_to_response, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.gis.geos import Point

def index(request):
    return render_to_response('index.html', {}, RequestContext(request))

@csrf_exempt
def create_issue(request):
    if request.method == 'POST':
        status = 'open'
        opener_id = request.POST.get('opener_id')
        description = request.POST.get('description')
        before_img = request.POST.get('before_img')
        category_id = request.POST.get('category_id')
        reported_to_311 = request.POST.get('reported_to_311')
        location_type_id = request.POST.get('location_type_id')
        longitude = request.POST.get('longitude')
        latitude = request.POST.get('latitude')
        pnt = Point(longitude, latitude)
        issue = Issue(status=status, opener_id=opener_id, description=description, before_img=before_img,
                      category_id=category_id, reported_to_311=reported_to_311, location_type_id=location_type_id,
                      geom=pnt)
        issue.save()
        return HttpResponse(json.dumps({'success':True}), content_type='application/json')
    else:
        return HttpResponse("you didn't POST any data, bro")


    # call create here
