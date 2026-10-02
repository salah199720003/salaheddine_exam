from django.urls import path

from . import views

urlpatterns = [
    path("", views.JokeListView.as_view(), name="joke_list"),
    path("create/", views.JokeCreateView.as_view(), name="joke_create"),
    path("<int:pk>/", views.JokeDetailView.as_view(), name="joke_detail"),
    path("<int:pk>/update/", views.JokeUpdateView.as_view(), name="joke_update"),
    path("<int:pk>/delete/", views.JokeDeleteView.as_view(), name="joke_delete"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
]
