from django.urls import path
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.base import RedirectView 
from sport_blog.views import *
from . import views


urlpatterns = [
	path('', Home.as_view(), name='home'),
	path('premierleague/', PremierLeague.as_view(), name='england'),
	path('spanishleague/', SpanishLeague.as_view(), name='spain'),
	path('italianleague/', ItalianLeague.as_view(), name='italy'),
	path('frenchleague/', FrenchLeague.as_view(), name='france'),
	path('bundasleague/', BundasLeague.as_view(), name='germany'),
	path('championsleague/', ChampionsLeague.as_view(), name='Champions'),
	path('contact/', Contact.as_view(), name='contact'),

]