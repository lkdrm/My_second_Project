import datetime
from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from pagecatalog.models import FilmOrder
from django.forms import ModelForm

class WasWatchedForm(forms.Form):
    was_watched_date = forms.DateField("Enter a date whe you have saw a film.")

    def clean_watched_date(self):
        data = self.cleaned_data["was_watched_date"]

        if data > datetime.date.today() + datetime.timedelta(days=1):
            raise ValidationError(_("Invalid date - you can`t choice"))

        return data
