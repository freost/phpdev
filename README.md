# Docker based PHP development environment

The PHP development environment supports PHP versions `7.4` through `8.5` and includes the following services:

| Service       | Container            | Port        | Description               | Enabled |
|---------------|----------------------|-------------|---------------------------|---------|
| beanstalkd    | phpdev-beanstalkd    | 11300       | Beanstalkd                | ❌      |
| mailpit       | phpdev-mailpit       | 8025        | SMTP, Mailpit             | ❌      |
| mariadb       | phpdev-mariadb       | 3306        | MariaDB                   | ❌      |
| mongo         | phpdev-mongo         | 27017       | MongoDB                   | ❌      |
| mongo         | phpdev-mongo-express | 8081        | Mongo Express             | ❌      |
| mysql         | phpdev-mysql         | 3307        | MySQL                     | ❌      |
|               | phpdev-nginx         | 8000        | Nginx                     | ✅      |
|               | phpdev               | -           | PHP-FPM                   | ✅      |
| postgres      | phpdev-postgresql    | 5432        | PostgreSQL                | ❌      |
| redis         | phpdev-redis         | 6379        | Redis                     | ✅      |
| redis         | phpdev-redis-insight | 13333       | Redis Insight             | ✅      |

-----------

## Setup

Run the following script to create the required directories:

```
python setup.py
```

> Use the `--htdocs-source` argument if you want to symlink `htdocs` to an existing directory.

## Configuration

The PHP version as well as the versions of most services can be set using the version variables in the `.env`file:

```
PHPDEV_PHP_VERSION=8.5
PHPDEV_POSTGRES_VERSION=18
PHPDEV_MARIADB_VERSION=12
```

> Note that some services may require their data path to be adjusted when switching versions (e.g. `PHPDEV_POSTGRES_DATA_PATH`).

## Starting

Starting the environment is done using the following command:

```
docker-compose up -d
```

> Images are built automatically on first start. Use `docker-compose up -d --build` to rebuild after changing a Dockerfile or switching versions.

Optional services can be permanently enabled by adding their profile name to the comma-separated `COMPOSE_PROFILES` variable in the `.env` file:

```
COMPOSE_PROFILES=redis,mongo,mysql
```

If you want to do a one-time start of a disabled service then you can enable its profile:

```
docker-compose --profile mongo up -d
```

> This starts the disabled service in addition to the enabled ones. You can also start a single service by name (e.g. `docker-compose up -d mongo`), which enables its profile automatically.

## Stopping

Stopping the environment is done using the following command:

```
docker-compose down
```
