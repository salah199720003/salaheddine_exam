from django.contrib import admin

from .models import Joke


@admin.register(Joke)
class JokeAdmin(admin.ModelAdmin):
    list_display = ("question", "user", "created_at", "updated_at")
    list_filter = ("created_at", "user")
    search_fields = ("question", "answer")
