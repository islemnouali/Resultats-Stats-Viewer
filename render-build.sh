#!/bin/bash
# Render-compatible Java installation for tabula-py

# 1. Download and extract Adoptium Temurin JDK 17 (smallest reliable JRE)
curl -L https://github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.11+9/OpenJDK17U-jre_x64_linux_hotspot_17.0.11_9.tar.gz -o jre.tar.gz
mkdir -p /opt/java
tar -xzf jre.tar.gz -C /opt/java --strip-components=1
rm jre.tar.gz

# 2. Set Java environment variables
export JAVA_HOME=/opt/java
export PATH=$JAVA_HOME/bin:$PATH
export LD_LIBRARY_PATH=$JAVA_HOME/lib/server:$LD_LIBRARY_PATH

# 3. Verify installation
echo "Java version:"
$JAVA_HOME/bin/java -version
echo "JVM library:"
ls -la $JAVA_HOME/lib/server/libjvm.so

# 4. Install Python dependencies
pip install -r requirements.txt

# 5. Collect static files
python manage.py collectstatic --noinput