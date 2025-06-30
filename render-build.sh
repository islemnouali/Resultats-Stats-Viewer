#!/usr/bin/env bash
set -o errexit

echo "Downloading Java..."

# Create temp java directory
mkdir -p /tmp/java

# Use a direct link to Adoptium (Eclipse Temurin) JDK 17 tar.gz
curl -L -o /tmp/openjdk.tar.gz https://github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.11%2B9/OpenJDK17U-jdk_x64_linux_hotspot_17.0.11_9.tar.gz

# Extract Java to /tmp/java
tar -xzf /tmp/openjdk.tar.gz -C /tmp/java --strip-components=1

# Export Java paths
export JAVA_HOME=/tmp/java
export PATH=$JAVA_HOME/bin:$PATH
export LD_LIBRARY_PATH=$JAVA_HOME/lib/server:$LD_LIBRARY_PATH

# Confirm installation
echo "Java version:"
$JAVA_HOME/bin/java -version

# Install python dependencies using Poetry
poetry install --no-root

# Django static files
python manage.py collectstatic --noinput
