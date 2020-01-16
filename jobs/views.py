from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from jobs.models import JobItem
from jobs.forms import JobForm

from redis import Redis
from rq import Queue
from mysearch import word_count

from django.views import View
# Create your views here.

class JobItemView(View):
    def post(self, request, *args, **kwargs):
        form = JobForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            url = cd['url']
            word = cd['search_word']
            q = Queue(connection=Redis())
            job = q.enqueue(word_count,args=(url, word),result_ttl=5000)
            JobItem.objects.create(
                    uuid=job.id,
                    status=job.get_status(),
                    url=url,
                    search_word=word
                    )



#           new_job = form.save(commit=False)
#           new_job.result = word_count(new_job.url, new_job.search_word)
            messages.success(request, 'Обождите')
#           new_job.save()
            return redirect(reverse('home'))
        return render(request, 'base.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = JobForm
        jobs = JobItem.objects.all()
        return render(request, 'base.html', {'form': form, 'jobs': jobs})
