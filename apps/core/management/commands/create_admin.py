from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create a new admin user if none exists'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.filter(is_superuser=True).exists():
            user = User.objects.create_superuser(
                username='selibeamy_admin',
                email='selwyn.cybersec@gmail.com',
                password='jd8zxj2z#i@oafklsado099ijk'
            )
            self.stdout.write(self.style.SUCCESS('Superuser created!'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists.')) 
