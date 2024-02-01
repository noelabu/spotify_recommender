FROM python:3.8.3
ENV SPOTIFY_RECOMMENDER app.py
COPY requirements.txt .env ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5005
CMD ["app.py"]