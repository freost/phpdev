FROM php:7.4-fpm

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

# Install exif support

RUN docker-php-ext-install exif

# Install xdebug

RUN pecl install xdebug
RUN docker-php-ext-enable xdebug

# Install pcntl

RUN docker-php-ext-configure pcntl --enable-pcntl
RUN docker-php-ext-install pdo pdo_mysql pcntl
