# 🌟 Professional Portfolio Website

A modern, elegant, and professional portfolio website built with Django (backend) and Bootstrap 5 (frontend), designed as a high-converting landing page for Upwork freelancers.

## ✨ Features

- **Hero Section** - Compelling headline and value proposition with call-to-action buttons
- **About Me** - Professional summary with tech stack badges
- **Projects Showcase** - Grid-based project gallery with detailed project pages
- **Markdown Content** - Rich markdown content support for detailed project descriptions
- **Analytics & Reports** - Showcase data-driven insights and dashboards
- **Services** - Comprehensive list of services offered
- **Why Hire Me** - Client-focused benefits and value propositions
- **Testimonials** - Client feedback and trust signals
- **Contact Form** - Django-powered contact form with admin panel
- **Fully Responsive** - Mobile-first design that works on all devices
- **SEO-Friendly** - Optimized structure and meta tags
- **Admin Panel** - Easy content management through Django admin

## 🛠️ Tech Stack

- **Backend**: Django 4.2.7
- **Frontend**: Bootstrap 5.3.2
- **JavaScript**: React 18 (for interactive components)
- **Database**: SQLite (default, easily switchable to PostgreSQL)
- **Image Handling**: Pillow
- **Forms**: Django Crispy Forms with Bootstrap 5
- **Markdown**: Python Markdown for rich content rendering

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## 🚀 Installation & Setup

### 1. Clone or navigate to the project directory

```bash
cd PortfolioApp
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (admin account)

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

### 6. Collect static files

```bash
python manage.py collectstatic --noinput
```

### 7. Run the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## 📝 Configuration

### Update Contact Information

1. Edit `templates/base.html` and `templates/contact/contact.html`
2. Replace `your.email@example.com` with your actual email
3. Replace `https://www.upwork.com/freelancers/~YOUR_PROFILE_ID` with your Upwork profile URL

### Update Social Links

Edit `templates/base.html` footer section to add your:
- GitHub profile
- LinkedIn profile
- Other social media links

### Django Settings

For production deployment, update `portfolio_site/settings.py`:

- Change `SECRET_KEY` to a secure random string
- Set `DEBUG = False`
- Update `ALLOWED_HOSTS` with your domain
- Configure email settings for contact form
- Set up a production database (PostgreSQL recommended)

## 📊 Adding Content

### Access Admin Panel

1. Visit `http://127.0.0.1:8000/admin/`
2. Login with your superuser credentials

### Add Projects

1. Go to **Portfolio > Projects**
2. Click **Add Project**
3. Fill in:
   - Title and slug (auto-generated from title)
   - Category (create categories first if needed)
   - Description, Problem, Solution, Result
   - Tech stack (comma-separated)
   - **Markdown Content** - Additional project details in Markdown format (supports code blocks, tables, lists, etc.)
   - Featured image
   - Live demo and GitHub URLs (optional)
   - Mark as "Featured" to show on homepage

**Note**: The Markdown Content field supports full Markdown syntax including:
- Headers, paragraphs, lists
- Code blocks with syntax highlighting
- Tables
- Blockquotes
- Links and images
- See `MARKDOWN_EXAMPLE.md` for a complete example

### Add Project Images

1. When editing a project, scroll to the **Project Images** section
2. Click **Add another Project image**
3. Upload images and add captions

### Add Categories

1. Go to **Portfolio > Categories**
2. Add category name, slug, and optional icon class (Bootstrap icons)

### Add Analytics Showcases

1. Go to **Portfolio > Analytics**
2. Add title, description, insights, impact, and optional image

### Add Testimonials

1. Go to **Portfolio > Testimonials**
2. Add client name, title, company, content, and rating
3. Mark as "Featured" to show on homepage

### View Contact Messages

1. Go to **Contact > Contact messages**
2. View and manage all contact form submissions

## 🎨 Customization

### Colors

Edit `static/css/style.css` to change the color scheme:

```css
:root {
    --primary-color: #0d6efd;
    --secondary-color: #6c757d;
    /* ... */
}
```

### Fonts

The site uses Google Fonts (Inter). To change, edit `templates/base.html`:

```html
<link href="https://fonts.googleapis.com/css2?family=YourFont:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

### Hero Section

Edit `templates/portfolio/home.html` to customize the hero section text and buttons.

## 📁 Project Structure

```
PortfolioApp/
├── contact/              # Contact app
│   ├── models.py        # ContactMessage model
│   ├── views.py         # Contact form view
│   ├── forms.py         # Contact form
│   └── admin.py         # Admin configuration
├── portfolio/           # Portfolio app
│   ├── models.py        # Project, Category, Analytics, Testimonial models
│   ├── views.py         # Home, project detail, projects list views
│   ├── admin.py         # Admin configuration
│   └── urls.py          # URL routing
├── portfolio_site/      # Django project settings
│   ├── settings.py      # Django settings
│   ├── urls.py          # Main URL configuration
│   └── wsgi.py          # WSGI configuration
├── templates/           # HTML templates
│   ├── base.html        # Base template
│   ├── portfolio/       # Portfolio templates
│   └── contact/         # Contact templates
├── static/              # Static files
│   ├── css/            # Stylesheets
│   └── js/             # JavaScript files
├── media/              # User-uploaded files (created after first upload)
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies
```

## 🚀 Deployment

### For Production

1. **Set Environment Variables**:
   ```bash
   export SECRET_KEY='your-secret-key-here'
   export DEBUG=False
   export ALLOWED_HOSTS='yourdomain.com,www.yourdomain.com'
   ```

2. **Use PostgreSQL** (recommended):
   - Update `DATABASES` in `settings.py`
   - Install `psycopg2-binary`

3. **Configure Static Files**:
   - Use WhiteNoise (already included) or a CDN
   - Run `python manage.py collectstatic`

4. **Set Up Web Server**:
   - Use Gunicorn or uWSGI with Nginx
   - Configure SSL/HTTPS

5. **Email Configuration**:
   - Update email settings in `settings.py` for contact form

### Popular Deployment Platforms

- **Heroku**: Add `Procfile` and `runtime.txt`
- **DigitalOcean**: Use App Platform or Droplet
- **AWS**: Use Elastic Beanstalk or EC2
- **PythonAnywhere**: Direct deployment

## 📱 Responsive Design

The website is fully responsive and tested on:
- Desktop (1920px+)
- Laptop (1024px - 1919px)
- Tablet (768px - 1023px)
- Mobile (320px - 767px)

## 🔒 Security Notes

- Change `SECRET_KEY` before deploying
- Set `DEBUG = False` in production
- Use environment variables for sensitive data
- Keep dependencies updated
- Use HTTPS in production
- Configure proper CORS settings if needed

## 📄 License

This project is open source and available for personal and commercial use.

## 🤝 Support

For issues or questions:
1. Check the Django documentation: https://docs.djangoproject.com/
2. Check Bootstrap documentation: https://getbootstrap.com/docs/5.3/
3. Review the code comments in the project files

## 🎯 Next Steps

1. Add your projects, testimonials, and analytics showcases
2. Customize the content to match your brand
3. Update contact information and social links
4. Test the contact form
5. Deploy to your preferred hosting platform

---

**Built with ❤️ for Upwork freelancers who want to stand out.**

