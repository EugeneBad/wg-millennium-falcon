from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Crate a superuser'

    def handle(self, *args, **options):
        u = User.objects.get(username='admin')

        if not u:
            u = User(username='admin')
        u.is_superuser = True
        u.is_staff = True
        u.save()
