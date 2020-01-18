from django.core.management import BaseCommand
from django.conf import settings 

from jobs.models import JobItem
from redis import Redis

class Command(BaseCommand):
    help = u'Updates the status of search tasks'

    def handle(self, *args, **kwargs):
        r = Redis(settings.REDIS_HOST, settings.REDIS_PORT)
        for entry in JobItem.objects.exclude(status='finished'):
            job = entry.get_job(redis_connection=r)
            entry.status = job.get_status()
            entry.result = job.result
            entry.save()
