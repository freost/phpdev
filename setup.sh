#!/usr/bin/env bash

set -euo pipefail

# Get path to current directory

CURRENT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Parse arguments

HTDOCS_SOURCE=""

usage() {
    echo "Usage: $0 [-s|--htdocs-source <path>]"
    echo ""
    echo "Setup script for the phpdev Docker environment."
    echo ""
    echo "  -s, --htdocs-source   The htdocs symlink source"
    exit 1
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        -s|--htdocs-source)
            HTDOCS_SOURCE="$2"
            shift 2
            ;;
        -h|--help)
            usage
            ;;
        *)
            echo "Unknown argument: $1"
            usage
            ;;
    esac
done

# Create php.env if it doesn't already exist

if [[ ! -f "$CURRENT_DIRECTORY/env/php.env" ]]; then
    cp "$CURRENT_DIRECTORY/env/php.env.dist" "$CURRENT_DIRECTORY/env/php.env"
fi

# Create .env if it doesn't already exist

if [[ ! -f "$CURRENT_DIRECTORY/.env" ]]; then
    cp "$CURRENT_DIRECTORY/.env.dist" "$CURRENT_DIRECTORY/.env"
fi

# Create htdocs if it doesn't already exist

HTDOCS="$CURRENT_DIRECTORY/htdocs"

if [[ ! -e "$HTDOCS" ]]; then
    if [[ -n "$HTDOCS_SOURCE" ]]; then
        HTDOCS_SOURCE="$(cd "$HTDOCS_SOURCE" 2>/dev/null && pwd || true)"

        if [[ -z "$HTDOCS_SOURCE" || ! -d "$HTDOCS_SOURCE" ]]; then
            echo "The htdocs symlink source does not exist!"
            exit 1
        fi

        echo "Symlinking htdocs to $HTDOCS_SOURCE."
        ln -s "$HTDOCS_SOURCE" "$HTDOCS"
    else
        echo "Creating $HTDOCS directory."
        mkdir "$HTDOCS"
    fi
fi

# Create the required storage directories

DIRECTORIES=(
    "$CURRENT_DIRECTORY/storage"
    "$CURRENT_DIRECTORY/storage/mariadb"
    "$CURRENT_DIRECTORY/storage/mysql"
    "$CURRENT_DIRECTORY/storage/mongodb"
    "$CURRENT_DIRECTORY/storage/postgres"
    "$CURRENT_DIRECTORY/storage/redis"
    "$CURRENT_DIRECTORY/storage/redis-insight"
)

for DIRECTORY in "${DIRECTORIES[@]}"; do
    if [[ ! -e "$DIRECTORY" ]]; then
        echo "Creating $DIRECTORY directory."
        mkdir "$DIRECTORY"
    fi
done

# Tell the user that we're done

echo "All done!"
