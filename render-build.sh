#!/usr/bin/env bash

# Install Java (OpenJDK 17)
sudo apt update
sudo apt install -y openjdk-17-jdk

# Set JAVA_HOME for Render
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64

# Optional: confirm Java installed
java -version
