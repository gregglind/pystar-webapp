# Create your views here.

from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.http import Http404

from polls.models import Poll

def redirect_to_polls(request):
    return HttpResponseRedirect('/polls/')

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render_to_response('polls/index.html', context)

def detail(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/detail.html', {'poll': p}, context_instance=RequestContext(request))

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll <strong>%s</strong>." % (poll_id,))

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % (poll_id,))

