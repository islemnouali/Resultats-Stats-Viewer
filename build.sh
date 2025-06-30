#!/bin/bash
# Install Java
apt-get update && apt-get install -y openjdk-11-jdk

# Install Python dependencies
pip install -r requirements.txt
python manage.py collectstatic --noinput