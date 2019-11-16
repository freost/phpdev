# Docker based PHP development environment

The PHP development environment starts the following Docker containers:

- phpdev (PHP + Apache, port 8000)
- phpdev-redis (Redis, port 6379)
- phpdev-postgres (Postgres, port 5432)
- phpdev-mariadb (MariaDB, port 3306)
- phpdev-mysql (MySQL, port 3307)

-----------

## Setup

Run the following script to create the required directories:

```
python setup.py
```

Build the Docker images using the following command:

```
docker-compose build
```

## Starting

Starting the environment is done using the following command:

```
docker-compose up -d
```

## Stopping

Stopping the environment is done using the following command:

```
docker-compose down
```
