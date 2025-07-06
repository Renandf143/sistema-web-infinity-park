#!/usr/bin/env python
"""
WSGI entry point for Django Infinity Park application.
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'infinity_park.settings')

# Get the WSGI application
application = get_wsgi_application()

# For Gunicorn compatibility
app = application