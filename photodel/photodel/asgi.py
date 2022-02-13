import django
import os
from channels.routing import get_default_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'photodel.settings')

django.setup()
application = get_default_application()
