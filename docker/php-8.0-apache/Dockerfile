FROM php:8.0-apache

RUN apt-get update

# Install OPcache support

RUN docker-php-ext-install opcache

# Install PosgreSQL support

RUN apt-get install -y libpq-dev
RUN docker-php-ext-install pdo_pgsql

# Install MySQL support

RUN docker-php-ext-install pdo pdo_mysql

# Install GD support

RUN apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libpng-dev
RUN docker-php-ext-configure gd --with-freetype --with-jpeg
RUN docker-php-ext-install -j$(nproc) gd

# Install xdebug

RUN pecl install xdebug
RUN docker-php-ext-enable xdebug

# Enable mod_rewrite

RUN a2enmod rewrite
