#!/usr/bin/env bash
set -o errexit

# Download and extract Java to /tmp/java
mkdir -p /tmp/java
curl -L -o /tmp/openjdk.tar.gz https://download.oracle.com/java/17/latest/jdk-17_linux-x64_bin.tar.gz
tar -xzf /tmp/openjdk.tar.gz -C /tmp/java --strip-components=1

# Set JAVA_HOME for the build process
export JAVA_HOME=/tmp/java
export PATH=$JAVA_HOME/bin:$PATH
export LD_LIBRARY_PATH=$JAVA_HOME/lib/server:$LD_LIBRARY_PATH

# Check if java is installed correctly
echo "Java version:"
$JAVA_HOME/bin/java -version

# Install Python deps
poetry install --no-root

# Run collectstatic if needed
python manage.py collectstatic --noinput
