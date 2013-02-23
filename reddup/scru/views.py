from .models import *
from django.template import Context, loader, RequestContext
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, render_to_response, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.gis.geos import Point
from vectorformats.Formats import Django, GeoJSON
from django.utils.safestring import SafeString


def index(request):
    return render_to_response('index.html', {}, RequestContext(request))


def all_issues(request):
    geoj = GeoJSON.GeoJSON()
    djf = Django.Django(geodjango='geom', properties=['description'])
    issues = geoj.encode(djf.decode(Issue.objects.filter(status='open')))
    print issues
    return render_to_response('mapview.html', {'issues': SafeString(issues)}, RequestContext(request))

@csrf_exempt
def open_issue(request):
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

        report = IssueUser(issue_id=issue.id, reporter_id=opener_id)
        report.save()

        return HttpResponse(json.dumps({'success': True}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'success': False}), content_type='application/json')


@csrf_exempt
def close_issue(request):
    if request.method == 'POST':
        issue_id = request.POST.get('issue_id')
        after_img = request.POST.get('after_img')
        status = 'closed'
        closer_id = request.POST.get('closer_id')
        cleaner_id = request.POST.get('cleaner_id')

        issue = Issue.objects.get(pk=issue_id)
        issue.after_img = after_img
        issue.status = status
        issue.closer_id = closer_id
        issue.cleaner_id = cleaner_id
        issue.save()
        return HttpResponse(json.dumps({'success': True}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'success': False}), content_type='application/json')


@csrf_exempt
def reup_issue(request):
    if request.method == 'POST':
        issue_id = request.POST.get('issue_id')
        reporter_id = request.POST.get('reporter_id')

        report = IssueUser(issue_id=issue_id, reporter_id=reporter_id)
        report.save()
        return HttpResponse(json.dumps({'success': True}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'success': False}), content_type='application/json')


@csrf_exempt
def create_pledge(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        longitude = request.POST.get('longitude')
        latitude = request.POST.get('latitude')
        pnt = Point(longitude, latitude)

        pledge = Pledge(user_id=user_id, geom=pnt)
        pledge.save()
        return HttpResponse(json.dumps({'success': True}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'success': False}), content_type='application/json')

@csrf_exempt
def claim_issue(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        issue_id = request.POST.get('issue_id')

        claim = Claim(user_id=user_id, issue_id=issue_id)
        claim.save()
        return HttpResponse(json.dumps({'success': True}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'success': False}), content_type='application/json')