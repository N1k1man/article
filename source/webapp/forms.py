from django import forms
from django.forms import widgets
from webapp.models import STATUS_CHOICES

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=50, required=True,   label='Title')
    author = forms.CharField(max_length=50, required=True, label='Author')
    content = forms.CharField(max_length=3000, required=True, label='Content', widget=widgets.Textarea(attrs={'cols':20, 'rows':5}))
    status = forms.ChoiceField(choices=STATUS_CHOICES, label='Status')
    publish_date = forms.DateField(label='Date', required=False, widget=widgets.DateInput(attrs={'type':'date'}))