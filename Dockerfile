FROM python:3.11.0-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install Java
RUN apt-get update && apt-get install -y openjdk-17-jre-headless && rm -rf /var/lib/apt/lists/*
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="$JAVA_HOME/bin:$PATH"

COPY requirements.txt /app/

RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install gunicorn

COPY . /app/

RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "firstProject.wsgi:application"]