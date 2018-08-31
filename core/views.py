from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from live.models import LiveMatch, Result
# Create your views here.

def to_home(request):
    return redirect('/home/')
def home(request):
    livematch = LiveMatch.objects.all()
    result = Result.objects.all()
    context = {
        'livematch': livematch,
        'result': result[0],
        'page': "2018 포카전",
    }
    return render(request, "page/home.html", context)

def about(request):
    livematch = LiveMatch.objects.all()
    result = Result.objects.all()
    context = {
        'livematch': livematch,
        'result': result[0],
        'page': "포카전이란?",
    }
    return render(request, "page/about.html", context)
def messages(request):
    livematch = LiveMatch.objects.all()
    result = Result.objects.all()
    context = {
        'livematch': livematch,
        'result': result[0],
        'page': "포카전 축사",
    }
    return render(request, "page/messages.html", context)

def soccer(request):
    livematch = LiveMatch.objects.all()
    result = Result.objects.all()
    context = {
        'livematch': livematch,
        'result': result[0],
        'page': "경기 - 축구",
    }
    return render(request, "page/sports/soccer.html", context)
def basketball(request):
    livematch = LiveMatch.objects.all()
    result = Result.objects.all()
    context = {
        'livematch': livematch,
        'result': result[0],
        'page': "경기 - 농구",
    }
    return render(request, "page/sports/basketball.html", context)
def baseball(request):
    livematch = LiveMatch.objects.all()
    result = Result.objects.all()
    context = {
        'livematch': livematch,
        'result': result[0],
        'page': "경기 - 야구",
    }
    return render(request, "page/sports/baseball.html", context)
def esports(request):
    livematch = LiveMatch.objects.all()
    result = Result.objects.all()
    context = {
        'livematch': livematch,
        'result': result[0],
        'page': "경기 - Esports",
    }
    return render(request, "page/sports/esports.html", context)
def quiz(request):
    livematch = LiveMatch.objects.all()
    result = Result.objects.all()
    context = {
        'livematch': livematch,
        'result': result[0],
        'page': "경기 - 과학퀴즈",
    }
    return render(request, "page/sports/quiz.html", context)
def ai(request):
    livematch = LiveMatch.objects.all()
    result = Result.objects.all()
    context = {
        'livematch': livematch,
        'result': result[0],
        'page': "경기 - A.I.",
    }
    return render(request, "page/sports/ai.html", context)
def badminton(request):
    livematch = LiveMatch.objects.all()
    result = Result.objects.all()
    context = {
        'livematch': livematch,
        'result': result[0],
        'page': "경기 - 배드민턴",
    }
    return render(request, "page/sports/badminton.html", context)
def hacking(request):
    livematch = LiveMatch.objects.all()
    result = Result.objects.all()
    context = {
        'livematch': livematch,
        'result': result[0],
        'page': "경기 - 해킹",
    }
    return render(request, "page/sports/hacking.html", context)

def cyber(request):
    livematch = LiveMatch.objects.all()
    result = Result.objects.all()
    context = {
        'livematch': livematch,
        'result': result[0],
        'page': "사이버포카전이란?",
    }
    return render(request, "page/cyber.html", context)
def starcraft(request):
    livematch = LiveMatch.objects.all()
    result = Result.objects.all()
    context = {
        'livematch': livematch,
        'result': result[0],
        'page': "사이버포카전 - 스타크래프트1",
    }
    return render(request, "page/cyber/starcraft.html", context)
def hearthstone(request):
    livematch = LiveMatch.objects.all()
    result = Result.objects.all()
    context = {
        'livematch': livematch,
        'result': result[0],
        'page': "사이버포카전 - 하스스톤",
    }
    return render(request, "page/cyber/hearthstone.html", context)
def heroes_of_the_storm(request):
    livematch = LiveMatch.objects.all()
    result = Result.objects.all()
    context = {
        'livematch': livematch,
        'result': result[0],
        'page': "사이버포카전 - 히오스",
    }
    return render(request, "page/cyber/heroes_of_the_storm.html", context)
def overwatch(request):
    livematch = LiveMatch.objects.all()
    result = Result.objects.all()
    context = {
        'livematch': livematch,
        'result': result[0],
        'page': "사이버포카전 - 오버워치",
    }
    return render(request, "page/cyber/overwatch.html", context)
def kartrider(request):
    livematch = LiveMatch.objects.all()
    result = Result.objects.all()
    context = {
        'livematch': livematch,
        'result': result[0],
        'page': "사이버포카전 - 카트라이더",
    }
    return render(request, "page/cyber/kartrider.html", context)
def battlegrounds(request):
    livematch = LiveMatch.objects.all()
    result = Result.objects.all()
    context = {
        'livematch': livematch,
        'result': result[0],
        'page': "사이버포카전 - 배틀그라운드",
    }
    return render(request, "page/cyber/battlegrounds.html", context)

def supporters(request):
    livematch = LiveMatch.objects.all()
    result = Result.objects.all()
    context = {
        'livematch': livematch,
        'result': result[0],
        'page': "포카전 서포터즈",
    }
    return render(request, "page/supporters.html", context)
def schedule(request):
    livematch = LiveMatch.objects.all()
    result = Result.objects.all()
    context = {
        'livematch': livematch,
        'result': result[0],
        'page': "일정 및 장소",
    }
    return render(request, "page/schedule.html", context)
def poapper(request):
    livematch = LiveMatch.objects.all()
    result = Result.objects.all()
    context = {
        'livematch': livematch,
        'result': result[0],
        'page': "만든 사람들",
    }
    return render(request, "page/poapper.html", context)


def error404(request):
    livematch = LiveMatch.objects.all()
    result = Result.objects.all()
    context = {
        'livematch': livematch,
        'result': result[0],
    }
    return render(request, "page/404.html", context)
def error500(request):
    livematch = LiveMatch.objects.all()
    result = Result.objects.all()
    context = {
        'livematch': livematch,
        'result': result[0],
    }
    return render(request, "page/500.html", context)
