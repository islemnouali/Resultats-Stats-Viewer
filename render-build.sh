#!/bin/bash
# Render build script for Django + tabula-py with Java support

# 1. Install OpenJDK 17 (smaller footprint than full JDK)
apt-get update && apt-get install -y openjdk-17-jdk-headless

# 2. Set explicit Java paths (critical for tabula-py)
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export LD_LIBRARY_PATH=$JAVA_HOME/lib/server:$LD_LIBRARY_PATH

# 3. Verify Java installation
echo "Java version:"
java -version
echo "JVM library path:"
ls -la $JAVA_HOME/lib/server/libjvm.so

# 4. Install Python dependencies
pip install -r requirements.txt

# 5. Collect static files
python manage.py collectstatic --noinput

# 6. Optional: Verify tabula-py can find Java
python -c "import jpype; print('JPype JVM path:', jpype.getDefaultJVMPath())"