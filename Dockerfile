
# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9-alpine3.13
ARG DATABASE_URL
ENV DATABASE_URL=$DATABASE_URL
ARG SECRET_KEY_DJANGO
ENV SECRET_KEY_DJANGO=$SECRET_KEY_DJANGO

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /bills-django
COPY . .
RUN python -m pip install -r requirements.txt


RUN adduser -u 5678 --disabled-password --gecos "" bills-djangouser && \
    chown -R bills-djangouser /bills-django
USER bills-djangouser

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi"]
