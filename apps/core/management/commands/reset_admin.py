from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Reset admin username and password'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        user = User.objects.filter(is_superuser=True).first()
        if user:
            user.username = 'selibeamy_admin'
            user.set_password('jd8zxj2z#i@oafklsado099ijk')
            user.save()
            self.stdout.write(self.style.SUCCESS('Admin credentials updated!'))
        else:
            self.stdout.write(self.style.ERROR('No superuser found!')) 