# Docker based PHP development environment

The PHP development environment includes the following services:

| Service    | Container         | Port        | Description  | Enabled |
|------------|-------------------|-------------|--------------|---------|
| beanstalkd | phpdev-beanstalkd | 11300       | Beanstalkd   | ✅      |
| mailhog    | phpdev-mailhog    | 8025, 10250 | Mailhog      | ✅      |
| mariadb    | phpdev-mariadb    | 3306        | MariaDB      | ❌      |
| mysql      | phpdev-mysql      | 3307        | MySQL        | ❌      |
| php        | phpdev            | 8000        | Apache + PHP | ✅      |
| postgres   | phpdev-postgres   | 5432        | PostgreSQL   | ❌      |
| redis      | phpdev-redis      | 6379        | Redis        | ✅      |

-----------

## Setup

Run the following script to create the required directories:

```
python setup.py
```

Build the Docker images using the following command:

```
docker compose build
```

## Starting

Starting the environment is done using the following command:

```
docker compose up -d
```

If you don't want to start all services then you can pass a list of the ones you want to use:

```
docker compose up -d php redis postgres
```

## Stopping

Stopping the environment is done using the following command:

```
docker compose down
```
