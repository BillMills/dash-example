FROM python:3.7
RUN pip install dash pandas
WORKDIR /app
COPY app.py /app/app.py
ENV FLASK_APP=app
CMD ["python", "app.py"]