from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("email",)
