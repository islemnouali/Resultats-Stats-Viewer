#!/usr/bin/env bash

# Download OpenJDK 17 from Eclipse Temurin
mkdir -p ~/.java

curl -L -o openjdk.tar.gz https://github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.11+9/OpenJDK17U-jdk_x64_linux_hotspot_17.0.11_9.tar.gz

# Extract it
tar -xzf openjdk.tar.gz -C ~/.java --strip-components=1

# Set JAVA_HOME and PATH
export JAVA_HOME="$HOME/.java"
export PATH="$JAVA_HOME/bin:$PATH"

# Confirm installation
java -version
