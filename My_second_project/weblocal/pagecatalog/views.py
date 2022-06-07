from django.shortcuts import render

# Create your views here.
import datetime
from django.shortcuts import get_list_or_404
from .models import Genre,Language,Producer,Film,FilmOrder,Actor
from django.views import View, generic
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

def index(request):
    num_films = Film.objects.all().count()
    num_films_ord = FilmOrder.objects.all().count()
    num_actors = Actor.objects.all().count()
    num_languages = Language.objects.all().count()
    num_of_genres = Genre.objects.all().count()
    num_of_producer = Producer.objects.all().count()

    num_visits = request.session.get("num_visits",0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_films" : num_films,
        "num_films_ord" : num_films_ord,
        "num_actors" : num_actors,
        "num_languages" : num_languages,
        "num_of_genres" : num_of_genres,
        "num_of_producer" : num_of_producer,
        "num_visits": num_visits,
    }

    return render(request, "pagecatalog/index.html", context=context)

class FilmListView(generic.ListView):
    model = Film

    paginate_by = 3
    context_object_name = "film_list"
    template_name = "pagecatalog/film_list.html"

    def get_context_data(self,**kwargs):
        context = super(FilmListView,self).get_context_data(**kwargs)
        context["data about film"] = "Some data about film"
        return context

class FilmDetailView(generic.DetailView):
    model = Film

    def film_detail_view(request, primary_key):
        film = get_list_or_404(Film,pk=primary_key)
        return render(request,"pagecatalog/film_detail.html",context={"film":film})

class ActorListView(generic.ListView):
    model = Actor

    paginate_by = 3
    context_object_name = "actor_list"
    template_name = "pagecatalog/actor_list.html"

    def get_context_data(self,**kwargs):
        context = super(ActorListView,self).get_context_data(**kwargs)
        context["data about film"] = "Some data about film"
        return context

class ActorDetailView(generic.DetailView):
    model = Actor

    def actor_detail_view(request,primary_key):
        actor = get_list_or_404(Actor, pk=primary_key)
        return render(request,"pagecatalog/actor_detail.html",context={"actor":actor})

class MyView(LoginRequiredMixin,View):
    permissions_required = 'pagecatalog.can_mark_returned'
    permissions_required = ('pagecatalog.can_mark_returned','pagecatalog.can_edit',)

class WatchedFilmsByUserListView(LoginRequiredMixin,generic.ListView):
    model = FilmOrder
    template_name = "pagecatalog/filmorder_list_watched.html"
    paginate_by = 2

    def get_queryset(self):
        return FilmOrder.objects.filter(was_watched_user=self.request.user).filter(status__exact="w").order_by("was_watched")
    
class FilmCreate(PermissionRequiredMixin,CreateView):
    model = Film
    fields = ["title","actor","description","genre","language","producer"]
    permission_required = "pagecatalog.can_mark_returned"

class FilmUpdate(PermissionRequiredMixin,UpdateView):
    model = Film
    fields = ["title","actor","description","genre","language","producer"]
    permission_required = "pagecatalog.can_mark_returned"

class FilmDelete(PermissionRequiredMixin,DeleteView):
    model = Film
    success_url = reverse_lazy("films")
    permission_required = "pagecatalog.can_mark_returned"

class ActorCreate(PermissionRequiredMixin,CreateView):
    model = Actor
    fields = ["first_name","last_name","date_of_birth","date_of_death","some_information"]
    permission_required = "pagecatalog.can_mark_returned"

class ActorUpdate(PermissionRequiredMixin,UpdateView):
    model = Actor
    fields = ["first_name","last_name","date_of_birth","date_of_death","some_information"]
    permission_required = "pagecatalog.can_mark_returned"

class ActorDelete(PermissionRequiredMixin,DeleteView):
    model = Actor
    success_url = reverse_lazy("actors")
    permission_required = "pagecatalog.can_mark_returned"
    