FROM openjdk:20-slim-bullseye AS get-cantaloupe

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update
RUN apt-get install -y unzip

WORKDIR /tmp

ADD https://github.com/cantaloupe-project/cantaloupe/releases/download/v5.0.5/cantaloupe-5.0.5.zip /tmp/cantaloupe.zip

RUN set -xe \
	&& unzip cantaloupe.zip

FROM --platform=linux/amd64 openjdk:20

WORKDIR /opt

COPY --from=get-cantaloupe /tmp/cantaloupe-5.0.5/cantaloupe-5.0.5.jar /opt/cantaloupe-5.0.5.jar
COPY --from=get-cantaloupe /tmp/cantaloupe-5.0.5/deps/Linux-x86-64 /opt/deps/Linux-x86-64

EXPOSE 8182

CMD [ "java", "-Dcantaloupe.config=cantaloupe.properties", "-Xms256m", "-Xmx8g", "-jar", "cantaloupe-5.0.5.jar" ]
