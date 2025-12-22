FROM php:8.5-fpm

RUN apt-get update

# Install PDO

RUN docker-php-ext-install pdo

# Install PosgreSQL support

RUN apt-get install -y libpq-dev
RUN docker-php-ext-install pdo_pgsql

# Install MySQL support

RUN docker-php-ext-install pdo_mysql

# Install GD support

RUN apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libpng-dev libwebp-dev libavif-dev
RUN docker-php-ext-configure gd --with-freetype --with-jpeg --with-webp --with-avif
RUN docker-php-ext-install -j$(nproc) gd

# Install Imagick support

RUN apt-get install -y imagemagick libmagickwand-dev
RUN pecl install imagick
RUN docker-php-ext-enable imagick

# Install exif support

RUN docker-php-ext-install exif

# Install xdebug

RUN pecl install xdebug
RUN docker-php-ext-enable xdebug

# Install pcntl

RUN docker-php-ext-configure pcntl --enable-pcntl
RUN docker-php-ext-install pdo pdo_mysql pcntl

# Configure pecl

RUN pecl config-set php_ini "${PHP_INI_DIR}/php.ini"

# Install MongoDB

RUN apt install libssl-dev
RUN pecl install --configureoptions='enable-ssl="yes"' mongodb
RUN echo "extension=mongodb.so" > "${PHP_INI_DIR}/conf.d/mongo.ini"

# Install APCu

RUN pecl install apcu
RUN docker-php-ext-enable apcu

# Install FFI

RUN apt-get install -y libffi-dev
RUN docker-php-ext-install ffi

# Install libexempi

RUN apt-get install exempi -y
