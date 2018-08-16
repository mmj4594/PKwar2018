from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
# Create your views here.

def to_home(request):
    return redirect('/home/')
def home(request):
    return render(request, "page/home.html")
def about(request):
    return render(request, "page/about.html")
def messages(request):
    return render(request, "page/messages.html")

def soccer(request):
    return render(request, "page/sports/soccer.html")
def basketball(request):
    return render(request, "page/sports/basketball.html")
def baseball(request):
    return render(request, "page/sports/baseball.html")
def esports(request):
    return render(request, "page/sports/esports.html")
def quiz(request):
    return render(request, "page/sports/quiz.html")
def ai(request):
    return render(request, "page/sports/ai.html")
def badminton(request):
    return render(request, "page/sports/badminton.html")
def hacking(request):
    return render(request, "page/sports/hacking.html")

def cyber(request):
    return render(request, "page/cyber.html")
def starcraft(request):
    return render(request, "page/cyber/starcraft.html")
def hearthstone(request):
    return render(request, "page/cyber/hearthstone.html")
def heroes_of_the_storm(request):
    return render(request, "page/cyber/heroes_of_the_storm.html")
def overwatch(request):
    return render(request, "page/cyber/overwatch.html")
def kartrider(request):
    return render(request, "page/cyber/kartrider.html")

def supporters(request):
    return render(request, "page/supporters.html")
def schedule(request):
    return render(request, "page/schedule.html")
def poapper(request):
    return render(request, "page/poapper.html")
def booth(request):
    return render(request, "page/booth.html")



def error404(request):
    return render(request, "page/404.html")
def error500(request):
    return render(request, "page/500.html")
