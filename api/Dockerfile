FROM python:3.10

WORKDIR /api

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#COPY requirements.txt .
COPY requirements.txt .

# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

#COPY . .
#COPY . ./data
COPY . /api
COPY main.py .

# gunicorn

EXPOSE 8000


#ENTRYPOINT ["streamlit", "run", "app/streamlit-app.py", "--server.port", "8080","--server.address","0.0.0.0"]
#ENTRYPOINT ["uvicorn", "main:app"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
#CMD ["uvicorn", "main:app", "--port", "8000"]

#ENTRYPOINT [ "streamlit", "run", "streamlit-app.py", "--server.port", "8080", "--browser.gatherUsageStats","false", "--server.runOnSave","true","--server.headless","true"]


