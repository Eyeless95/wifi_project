import os

import dotenv
from django.core.wsgi import get_wsgi_application

dotenv.load_dotenv(dotenv.find_dotenv())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wifi.settings")

application = get_wsgi_application()
