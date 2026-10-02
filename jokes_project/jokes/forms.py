from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Joke


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Enter a valid email address.")

    class Meta:
        model = User
        fields = ("username", "email")


class JokeForm(forms.ModelForm):
    class Meta:
        model = Joke
        fields = ("question", "answer")
        widgets = {
            "question": forms.TextInput(
                attrs={"placeholder": "Why did the chicken cross the road?"}
            ),
            "answer": forms.Textarea(
                attrs={"placeholder": "To get to the other side!"}
            ),
        }
