from django.apps import AppConfig
import os
import pandas as pd
from django.conf import settings

class StudentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'students'
