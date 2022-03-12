FROM python:3.8

EXPOSE 5000

RUN apt-get update -y \
    && apt-get install -y \
        libpq-dev \
        wait-for-it \
        iproute2 \
    && apt-get autoremove

WORKDIR /cfp_v3/backend

COPY Pipfile Pipfile.lock ./

RUN pip install --upgrade pip \
    && pip install pipenv==v2020.11.15 \
    && pipenv install --dev --system --deploy --verbose

ADD . /cfp_v3/backend

ENTRYPOINT ["bash", "docker-entrypoint.sh"]
