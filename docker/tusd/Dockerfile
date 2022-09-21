FROM php:8.1-cli AS tusd-binary

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

WORKDIR /tmp

ADD https://github.com/tus/tusd/releases/download/v1.9.2/tusd_linux_arm64.tar.gz /tmp/tusd.tar.gz

RUN set -xe \
    && echo "a6b45b6bed96d9ee6202dfb18f480c7c2c316504d9ad85581e843aabddee3829 *tusd.tar.gz" | sha256sum -c - \
    && tar -xvf tusd.tar.gz

FROM php:8.1-cli

RUN apt-get update

RUN apt-get install -y libpq-dev
RUN docker-php-ext-install pdo_pgsql

COPY --from=tusd-binary /tmp/tusd_linux_arm64/tusd /usr/local/bin/tusd

EXPOSE 1080

CMD [ "/usr/local/bin/tusd", "--hooks-dir", "/archive-digitisation/bin/tus-hooks", "--upload-dir", "/data/tus/uploads" ]
