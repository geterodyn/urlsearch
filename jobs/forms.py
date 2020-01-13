from django import forms

from jobs.models import JobItem

class JobForm(forms.ModelForm):
    class Meta:
        model = JobItem
        fields = ('url', 'search_word')
        labels = {'url': 'URL страницы', 'search_word': 'искомое слово'}