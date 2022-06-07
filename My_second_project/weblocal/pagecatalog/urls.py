from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("films/", views.FilmListView.as_view(), name = "films"),
    path("film/<int:pk>", views.FilmDetailView.as_view(), name="film-detail"),
    path("actors/", views.ActorListView.as_view(), name="actors"),
    path("actor/<int:pk>", views.ActorDetailView.as_view(), name="actor-detail"),
    path("myfilms/", views.WatchedFilmsByUserListView.as_view(), name="my-watched"),
    path("film/create/", views.FilmCreate.as_view(), name="film-create"),
    path("film/<int:pk>/update/", views.FilmUpdate.as_view(), name="film-update"),
    path("film/<int:pk>/delete/", views.FilmDelete.as_view(), name="film-delete"),
    path("actor/create/", views.ActorCreate.as_view(), name="actor-create"),
    path("actor/<int:pk>/update/", views.FilmUpdate.as_view(), name="actor-update"),
    path("actor/<int:pk>/delete/", views.FilmDelete.as_view(), name="actor-delete"),
]
