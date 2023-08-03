FROM python:3.10

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#COPY requirements.txt .
COPY /app . 
COPY /app/requirements.txt .

# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

#COPY . .
#COPY . ./data
COPY . /app

# gunicorn

EXPOSE 8080


HEALTHCHECK CMD curl --fail http://localhost:8080/_stcore/health


ENTRYPOINT ["streamlit", "run", "app/streamlit-app.py", "--server.port", "8080","--server.address","0.0.0.0"]
#ENTRYPOINT ["streamlit", "run", "streamlit-app.py", "--server.port", "8080"]

#ENTRYPOINT [ "streamlit", "run", "streamlit-app.py", "--server.port", "8080", "--browser.gatherUsageStats","false", "--server.runOnSave","true","--server.headless","true"]


