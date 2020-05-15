from django import forms
from app_models.models import AnonymousComments

class AnonymousCommentsForm(forms.ModelForm):
    class Meta:
        model = AnonymousComments
        fields = '__all__'
