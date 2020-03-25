from django.shortcuts import redirect
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import render
from sport_blog.models import *



class Home(ListView):
    template_name = 'sport_blog/home.html'
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    queryset1 = MiniPost.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['posts'] = self.queryset
        context['miniposts'] = self.queryset1
        return context


class PremierLeague(ListView):
    template_name = 'sport_blog/premier_league.html'
    queryset = Post.objects.filter(league='PL').order_by('published_date')
    queryset1 = MiniPost.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PremierLeague, self).get_context_data(**kwargs)
        context['posts'] = self.queryset
        context['miniposts'] = self.queryset1
        return context


class SpanishLeague(ListView):
    template_name = 'sport_blog/spanish_league.html'
    queryset = Post.objects.filter(league='LL').order_by('published_date')
    queryset1 = MiniPost.objects.all()

    def get_context_data(self, **kwargs):
        context = super(SpanishLeague, self).get_context_data(**kwargs)
        context['posts'] = self.queryset
        context['miniposts'] = self.queryset1
        return context


class ItalianLeague(ListView):
    template_name = 'sport_blog/italian_league.html'
    queryset = Post.objects.filter(league='SA').order_by('published_date')
    queryset1 = MiniPost.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ItalianLeague, self).get_context_data(**kwargs)
        context['posts'] = self.queryset
        context['miniposts'] = self.queryset1
        return context


class FrenchLeague(ListView):
    template_name = 'sport_blog/french_league.html'
    queryset = Post.objects.filter(league='L1').order_by('published_date')
    queryset1 = MiniPost.objects.all()

    def get_context_data(self, **kwargs):
        context = super(FrenchLeague, self).get_context_data(**kwargs)
        context['posts'] = self.queryset
        context['miniposts'] = self.queryset1
        return context


class BundasLeague(ListView):
    template_name = 'sport_blog/bundas_league.html'
    queryset = Post.objects.filter(league='BL').order_by('published_date')
    queryset1 = MiniPost.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BundasLeague, self).get_context_data(**kwargs)
        context['posts'] = self.queryset
        context['miniposts'] = self.queryset1
        return context


class ChampionsLeague(ListView):
    template_name = 'sport_blog/champions_league.html'
    queryset = Post.objects.filter(league='CL').order_by('published_date')
    queryset1 = MiniPost.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ChampionsLeague, self).get_context_data(**kwargs)
        context['posts'] = self.queryset
        context['miniposts'] = self.queryset1
        return context


class Contact(TemplateView):
    template_name = 'sport_blog/contact.html'


	

