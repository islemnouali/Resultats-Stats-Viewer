#!/bin/bash
# Install OpenJDK 17 (explicitly specify JVM headless + full JDK)
apt-get update && apt-get install -y openjdk-17-jdk-headless

# Set JAVA_HOME explicitly (Render uses Ubuntu 22.04)
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export LD_LIBRARY_PATH=$JAVA_HOME/lib/server:$LD_LIBRARY_PATH

# Verify Java installation
java -version
ls -la $JAVA_HOME/lib/server/libjvm.so  # Check if JVM library exists

# Install Python dependencies
pip install -r requirements.txt
python manage.py collectstatic --noinput