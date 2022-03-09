FROM python:3.9

ENV DEBIAN_FRONTEND="noninteractive"
RUN apt-get update \
 && apt-get install --yes --no-install-recommends \
        gosu \
        wait-for-it \
 \
 && rm -rf /var/lib/apt/lists/* \
           /tmp/*

WORKDIR /etc/phonebook

COPY Pipfile /etc/phonebook/
COPY Pipfile.lock /etc/phonebook/

RUN pip install --no-cache-dir \
        pipenv \
 \
 && pipenv install --clear \
                   --deploy \
                   --system \
                   --verbose

WORKDIR /opt/phonebook

ENV PGHOST="host.docker.internal"
ENV PGPORT="5432"
ENV PGUSER="phonebook"
ENV PGPASSWORD=""
ENV PGDATABASE="phonebook"

COPY ./src/ /opt/phonebook/
COPY entrypoint.sh /

RUN useradd --home /home/phonebook --create-home \
            --comment "Phonebook" \
            --user-group phonebook \
 \
 && ln -s /etc/phonebook/ /home/phonebook/config \
 && ln -s /opt/phonebook/ /home/phonebook/source

ENTRYPOINT ["/entrypoint.sh"]
CMD ["phonebook"]

EXPOSE 8080
