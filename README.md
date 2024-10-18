# Docker based PHP development environment

The PHP development environment includes the following services:

| Service       | Container            | Port        | Description   | Enabled |
|---------------|----------------------|-------------|---------------|---------|
| beanstalkd    | phpdev-beanstalkd    | 11300       | Beanstalkd    | ❌      |
| mailhog       | phpdev-mailhog       | 8025, 10250 | Mailhog       | ❌      |
| mariadb       | phpdev-mariadb       | 3306        | MariaDB       | ❌      |
| mongo         | phpdev-mongodb       | 27017       | MongoDB       | ❌      |
| mongo-express | phpdev-mongo-express | 8081        | Mongo Express | ❌      |
| mysql         | phpdev-mysql         | 3307        | MySQL         | ❌      |
| php           | phpdev               | 8000        | Apache + PHP  | ✅      |
| postgres      | phpdev-postgres      | 5432        | PostgreSQL    | ❌      |
| redis         | phpdev-redis         | 6379, 13333 | Redis         | ✅      |

-----------

## Setup

Run the following script to create the required directories:

```
python setup.py
```

> Use the `--htdocs-source` argument if you want to symlink `htdocs` to an existing directory.

Build the Docker images using the following command:

```
docker-compose build
```

## Starting

Starting the environment is done using the following command:

```
docker-compose up -d
```

If you don't want to start all enabled services then you can pass a list of the ones you want to use:

```
docker-compose up -d php
```

## Stopping

Stopping the environment is done using the following command:

```
docker-compose down
```
