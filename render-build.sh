#!/usr/bin/env bash

# Download and extract OpenJDK 17
mkdir -p ~/.java
curl -L -o openjdk.tar.gz https://download.bell-sw.com/java/17.0.11+9/bellsoft-jdk17.0.11+9-linux-amd64.tar.gz
tar -xzf openjdk.tar.gz -C ~/.java --strip-components=1

# Set JAVA_HOME and update PATH
export JAVA_HOME="$HOME/.java"
export PATH="$JAVA_HOME/bin:$PATH"

# Confirm it works
java -version
