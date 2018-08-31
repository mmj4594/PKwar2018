from django.conf.urls import url, handler400, handler403, handler404, handler500
from . import views


urlpatterns = [
    url(r'^$', views.to_home),
    url(r'^home/$', views.home),
    url(r'^about/$', views.about),
    url(r'^messages/$', views.messages),

    url(r'^sports/soccer/$', views.soccer),
    url(r'^sports/basketball/$', views.basketball),
    url(r'^sports/baseball/$', views.baseball),
    url(r'^sports/esports/$', views.esports),
    url(r'^sports/quiz/$', views.quiz),
    url(r'^sports/ai/$', views.ai),
    url(r'^sports/badminton/$', views.badminton),
    url(r'^sports/hacking/$', views.hacking),

    url(r'^cyber/$', views.cyber),
    url(r'^cyber/starcraft/$', views.starcraft),
    url(r'^cyber/kartrider/$', views.kartrider),
    url(r'^cyber/overwatch/$', views.overwatch),
    url(r'^cyber/heroes_of_the_storm/$', views.heroes_of_the_storm),
    url(r'^cyber/hearthstone/$', views.hearthstone),
    url(r'^cyber/battlegrounds/$', views.battlegrounds),

    url(r'^supporters/$', views.supporters),
    url(r'^schedule/$', views.schedule),
    url(r'^poapper/$', views.poapper),
]
