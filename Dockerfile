FROM python:3.12

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim

RUN useradd -rms /bin/bash www && chmod 777 /opt /run

WORKDIR /digital-snowboarding

RUN  mkdir /digital-snowboarding/media && chown -R www:www /digital-snowboarding && chmod 755 /digital-snowboarding

COPY --chown=www:www . .

RUN pip install -r requirements.txt

USER www

CMD ["uvicorn","config.wsgi:application", "--host", "0.0.0.0", "--port", "8080", "--workers", "5"]