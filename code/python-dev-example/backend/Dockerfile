FROM python:3.11-slim-bullseye

# Copy python requirements
COPY ./requirements.txt /

# Install dependencies and install python packages
RUN apt-get update &&\
    apt-get install -y --no-install-recommends tzdata libudev-dev -y &&\
    python3 -m pip install --upgrade --no-cache-dir pip &&\
    python3 -m pip install --upgrade --no-cache-dir -r requirements.txt &&\
    rm -rf /var/lib/apt/lists/* && mkdir /App

# Set new work directory
WORKDIR /App

# Copy app
COPY ./src/main.py ./
COPY ./src/sql_manager.py ./

# Start application
ENTRYPOINT ["python", "main.py"]