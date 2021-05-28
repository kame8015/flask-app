FROM python:3.8.5

RUN pip install Flask==2.0.1

COPY app.py .

CMD ["python", "app.py"]