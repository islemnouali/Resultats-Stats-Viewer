#!/bin/bash
export JAVA_HOME=/tmp/java
export LD_LIBRARY_PATH=$JAVA_HOME/lib/server
export PATH=$JAVA_HOME/bin:$PATH

gunicorn firstProject.wsgi
