from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import JokeForm, SignUpForm
from .models import Joke


class JokeListView(ListView):
    model = Joke
    template_name = "jokes/joke_list.html"
    context_object_name = "jokes"


class JokeDetailView(DetailView):
    model = Joke
    template_name = "jokes/joke_detail.html"
    context_object_name = "joke"


class JokeCreateView(LoginRequiredMixin, CreateView):
    model = Joke
    form_class = JokeForm
    template_name = "jokes/joke_form.html"
    success_url = reverse_lazy("joke_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class JokeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Joke
    form_class = JokeForm
    template_name = "jokes/update_joke.html"
    success_url = reverse_lazy("joke_list")

    def test_func(self):
        return self.get_object().user == self.request.user


class JokeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Joke
    template_name = "jokes/delete_joke.html"
    context_object_name = "joke"
    success_url = reverse_lazy("joke_list")

    def test_func(self):
        return self.get_object().user == self.request.user


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
