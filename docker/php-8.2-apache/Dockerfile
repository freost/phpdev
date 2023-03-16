FROM php:8.2-apache

RUN apt-get update

# Install OPcache support

RUN docker-php-ext-install opcache

# Install PDO

RUN docker-php-ext-install pdo

# Install PosgreSQL support

RUN apt-get install -y libpq-dev
RUN docker-php-ext-install pdo_pgsql

# Install MySQL support

RUN docker-php-ext-install pdo_mysql

# Install GD support

RUN apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libpng-dev
RUN docker-php-ext-configure gd --with-freetype --with-jpeg
RUN docker-php-ext-install -j$(nproc) gd

# Install xdebug

RUN pecl install xdebug
RUN docker-php-ext-enable xdebug

# Install pcntl

RUN docker-php-ext-configure pcntl --enable-pcntl
RUN docker-php-ext-install pdo pdo_mysql pcntl

# Install MongoDB

RUN pecl config-set php_ini "${PHP_INI_DIR}/php.ini"
RUN pecl install mongodb
RUN echo "extension=mongodb.so" > "${PHP_INI_DIR}/conf.d/mongo.ini"

# Enable mod_rewrite

RUN a2enmod rewrite
