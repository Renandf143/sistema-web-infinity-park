#!/usr/bin/env python
"""
WSGI config for Infinity Park Django project.

This module contains the WSGI application used by Django's runserver.
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'infinity_park.settings')

application = get_wsgi_application()