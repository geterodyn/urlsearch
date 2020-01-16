from django.core.management import BaseCommand

from jobs.models import JobItem
from redis import Redis
from rq.job import Job

class Command(BaseCommand):
    help = u'Updates the status of search tasks'

    def handle(self, *args, **kwargs):
        r = Redis()
        entries = JobItem.objects.exclude(status='finished')
        for entry in entries:
            str_uuid = entry.uuid.urn[9:]
            job = Job.fetch(str_uuid, connection=r)
            entry.status = job.get_status()
            entry.result = job.result
            entry.save()
