from django.forms import ModelForm
from .models import Winner

class WinnerForm(ModelForm):
  class Meta:
    model = Winner
    fields = ["winner", "date", "win"]