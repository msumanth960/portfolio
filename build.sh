#!/usr/bin/env bash
# Exit on error
set -o errexit

# Upgrade pip and build tools
pip install --upgrade pip setuptools wheel

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

