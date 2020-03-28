from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import render
from sport_blog.models import *


class HomeView(TemplateView):
    template_name = 'sport_blog/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('published_date')
        context['miniposts'] = MiniPost.objects.all()
        return context


class PremierLeagueView(TemplateView):
    template_name = 'sport_blog/premier_league.html'

    def get_context_data(self, **kwargs):
        context = super(PremierLeagueView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(league='PL').order_by('published_date')
        context['miniposts'] = MiniPost.objects.all()
        return context



class SpanishLeagueView(TemplateView):
    template_name = 'sport_blog/spanish_league.html'

    def get_context_data(self, **kwargs):
        context = super(SpanishLeagueView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(league='LL').order_by('published_date')
        context['miniposts'] = MiniPost.objects.all()
        return context


class ItalianLeagueView(TemplateView):
    template_name = 'sport_blog/italian_league.html'

    def get_context_data(self, **kwargs):
        context = super(ItalianLeagueView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(league='SA').order_by('published_date')
        context['miniposts'] = MiniPost.objects.all()
        return context


class FrenchLeagueView(TemplateView):
    template_name = 'sport_blog/french_league.html'

    def get_context_data(self, **kwargs):
        context = super(FrenchLeagueView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(league='L1').order_by('published_date')
        context['miniposts'] = MiniPost.objects.all()
        return context


class BundasLeagueView(TemplateView):
    template_name = 'sport_blog/bundas_league.html'

    def get_context_data(self, **kwargs):
        context = super(BundasLeagueView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(league='BL').order_by('published_date')
        context['miniposts'] = MiniPost.objects.all()
        return context


class ChampionsLeagueView(TemplateView):
    template_name = 'sport_blog/champions_league.html'

    def get_context_data(self, **kwargs):
        context = super(ChampionsLeagueView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(league='CL').order_by('published_date')
        context['miniposts'] = MiniPost.objects.all()
        return context


class ContactView(TemplateView):
    template_name = 'sport_blog/contact.html'



