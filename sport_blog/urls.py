from django.urls import path
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.base import RedirectView 
from sport_blog.views import *
from . import views


urlpatterns = [
	path('', HomeView.as_view(template_name='sport_blog/home.html'), name="home"),
	path('premierleague/', PremierLeagueView.as_view(template_name='sport_blog/premier_league.html'), name='england'),
	path('spanishleague/', SpanishLeagueView.as_view(template_name='sport_blog/spanish_league.html'), name='spain'),
	path('italianleague/', ItalianLeagueView.as_view(template_name='sport_blog/italian_league.html'), name='italy'),
	path('frenchleague/', FrenchLeagueView.as_view(template_name='sport_blog/french_league.html'), name='france'),
	path('bundasleague/', BundasLeagueView.as_view(template_name='sport_blog/bundas_league.html'), name='germany'),
	path('championsleague/', ChampionsLeagueView.as_view(template_name='sport_blog/champions_league.html'), name='Champions'),
	path('contactpage/', ContactView.as_view(template_name='sport_blog/contact.html'), name='contact'),

]