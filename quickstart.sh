#!/bin/bash

# Quick Start Script for Portfolio Website

echo "🌟 Portfolio Website - Quick Start"
echo "=================================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -q -r requirements.txt

# Run migrations
echo "Running database migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Check if superuser exists
echo ""
echo "Checking for admin user..."
python manage.py shell << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(is_superuser=True).exists():
    print("⚠️  No superuser found. Creating one...")
    print("Please run: python manage.py createsuperuser")
else:
    print("✅ Superuser exists")
EOF

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Create a superuser: python manage.py createsuperuser"
echo "2. Run the server: python manage.py runserver"
echo "3. Visit http://127.0.0.1:8000/"
echo "4. Access admin at http://127.0.0.1:8000/admin/"
echo ""

