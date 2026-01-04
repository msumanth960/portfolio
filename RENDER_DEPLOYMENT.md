# Render Deployment Guide

This guide will help you deploy your Django portfolio website to Render.

## Prerequisites

1. A GitHub account with your code pushed to the repository
2. A Render account (sign up at https://render.com)
3. A Neon database (already configured)

## Step-by-Step Deployment

### 1. Push Your Code to GitHub

Make sure your code is pushed to: https://github.com/msumanth960/portfolio

### 2. Create a New Web Service on Render

1. Go to https://dashboard.render.com
2. Click "New +" → "Web Service"
3. Connect your GitHub account if not already connected
4. Select your repository: `msumanth960/portfolio`
5. Configure the service:
   - **Name**: `portfolio-app` (or your preferred name)
   - **Region**: Choose closest to your users
   - **Branch**: `main`
   - **Root Directory**: Leave empty (or `./` if needed)
   - **Runtime**: `Python 3`
   - **Python Version**: `3.11.0` (IMPORTANT: Set this in Environment Variables or use runtime.txt)
   - **Build Command**: 
     ```bash
     pip install --upgrade pip setuptools wheel && pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
     ```
   - **Start Command**: 
     ```bash
     gunicorn portfolio_site.wsgi:application
     ```

### 3. Configure Environment Variables

In the Render dashboard, go to your service → Environment → Add the following:

- **DATABASE_URL**: Your Neon database connection string
  ```
  postgresql://username:password@hostname.neon.tech/database?sslmode=require
  ```
- **SECRET_KEY**: Generate a secure secret key (you can use: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`)
- **DEBUG**: `False`
- **ALLOWED_HOSTS**: `your-app-name.onrender.com` (Render will provide the URL)
- **PYTHON_VERSION**: `3.11.0` (optional, but recommended)
- **CLOUDINARY_CLOUD_NAME**: Your Cloudinary cloud name (from Cloudinary dashboard)
- **CLOUDINARY_API_KEY**: Your Cloudinary API key (from Cloudinary dashboard)
- **CLOUDINARY_API_SECRET**: Your Cloudinary API secret (from Cloudinary dashboard)

### 4. Deploy

1. Click "Create Web Service"
2. Render will automatically:
   - Clone your repository
   - Install dependencies
   - Run migrations
   - Collect static files
   - Start your application

### 5. Create a Superuser (After Deployment)

Once deployed, you need to create a superuser to access the admin panel:

1. Go to your service → Shell
2. Run:
   ```bash
   python manage.py createsuperuser
   ```
3. Follow the prompts to create your admin account

### 6. Access Your Site

- Your site will be available at: `https://your-app-name.onrender.com`
- Admin panel: `https://your-app-name.onrender.com/admin/`

## Important Notes

1. **Database**: Make sure your Neon database is accessible from Render's servers
2. **Static Files**: WhiteNoise is configured to serve static files
3. **Media Files**: For production, consider using AWS S3 or Cloudinary for media storage
4. **SSL**: Render provides free SSL certificates automatically
5. **Auto-Deploy**: Render will automatically redeploy when you push to your main branch

## Troubleshooting

### Build Fails
- Check the build logs in Render dashboard
- Ensure all dependencies are in `requirements.txt`
- Verify Python version compatibility

### Database Connection Issues
- Verify your `DATABASE_URL` is correct
- Check if Neon allows connections from Render's IPs
- Ensure SSL mode is set to `require` in connection string

### Static Files Not Loading
- Verify `collectstatic` ran successfully
- Check WhiteNoise configuration in settings
- Ensure `STATIC_ROOT` is set correctly

### 500 Errors
- Check application logs in Render dashboard
- Verify `DEBUG=False` and check `ALLOWED_HOSTS`
- Ensure all environment variables are set

## Custom Domain (Optional)

1. Go to your service → Settings → Custom Domain
2. Add your domain
3. Follow DNS configuration instructions
4. Update `ALLOWED_HOSTS` to include your custom domain

## Monitoring

- View logs: Service → Logs
- Monitor metrics: Service → Metrics
- Set up alerts: Service → Alerts

---

**Your portfolio is now live!** 🚀

