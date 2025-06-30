#!/usr/bin/env bash
# Install OpenJDK 11 (recommended for stability)
apt-get update && apt-get install -y openjdk-11-jdk

# Verify installation (optional, helps debug)
java -version
javac -version

