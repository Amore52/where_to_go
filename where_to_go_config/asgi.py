import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'where_to_go_config.settings')

application = get_asgi_application()
