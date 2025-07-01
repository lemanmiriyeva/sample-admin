# api/index.py

from django.core.wsgi import get_wsgi_application

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dashboard_project.settings')

# This is the WSGI app Vercel will call
app = get_wsgi_application()
