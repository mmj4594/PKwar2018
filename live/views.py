from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from .models import LiveMatch, FinishedMatch, Result


def index(request):
    livematch = LiveMatch.objects.all()
    matches = FinishedMatch.objects.all()
    result = Result.objects.all()
    context = {
        'livematch': livematch,
        'matches': matches,
        'result': result[0],
    }
    return render(request, "chat/index.html", context)


def reload_match(request):
    livematch = LiveMatch.objects.all()
    context = {
        'livematch': livematch,
    }
    return render(request, 'chat/reload_match.html', context)
