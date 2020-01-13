from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from jobs.models import JobItem
from jobs.forms import JobForm

import requests

from django.views import View
# Create your views here.

def word_count(url, word):
    response = requests.get(url)
    words_list = response.text.split()
    return words_list.count(word)

class JobItemView(View):
    def post(self, request, *args, **kwargs):
        form = JobForm(request.POST)
        if form.is_valid():
            new_job = form.save(commit=False)
            new_job.result = word_count(new_job.url, new_job.search_word)
            messages.success(request, 'Обождите')
            new_job.save()
            return redirect(reverse('home'))
        return render(request, 'base.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = JobForm
        jobs = JobItem.objects.all()
        return render(request, 'base.html', {'form': form, 'jobs': jobs})