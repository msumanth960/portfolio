# Cloudinary Integration Guide

This project uses Cloudinary for media storage (images, files). This guide will help you set up Cloudinary.

## Why Cloudinary?

- **Free tier**: 25GB storage and 25GB bandwidth per month
- **Automatic image optimization**: Resize, crop, and optimize images on-the-fly
- **CDN delivery**: Fast global content delivery
- **No server storage needed**: Media files stored in the cloud
- **Easy integration**: Simple Django integration

## Setup Instructions

### 1. Create a Cloudinary Account

1. Go to https://cloudinary.com/users/register/free
2. Sign up for a free account (you can use Google, GitHub, or email)
3. Verify your email address

### 2. Get Your Cloudinary Credentials

After signing up, you'll be redirected to the Cloudinary Dashboard:

1. Copy your **Cloud Name** (visible at the top of the dashboard)
2. Go to **Settings** → **Security** (or click "Dashboard" → "Account Details")
3. Copy your **API Key** and **API Secret**

### 3. Configure Environment Variables

#### For Local Development (.env file)

Create or update your `.env` file in the project root:

```env
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

#### For Render Deployment

1. Go to your Render service dashboard
2. Navigate to **Environment** section
3. Add the following environment variables:
   - `CLOUDINARY_CLOUD_NAME`: Your cloud name
   - `CLOUDINARY_API_KEY`: Your API key
   - `CLOUDINARY_API_SECRET`: Your API secret

### 4. Install Dependencies

Dependencies are already in `requirements.txt`. If installing locally:

```bash
pip install -r requirements.txt
```

### 5. Migrate Database (if needed)

If you've already created projects with images, you may need to migrate:

```bash
python manage.py migrate
```

### 6. Test the Integration

1. Go to Django admin: http://localhost:8000/admin/
2. Create a new Project
3. Upload a featured image
4. The image should now be stored on Cloudinary instead of local storage

## How It Works

- **Image Upload**: When you upload images through Django admin or forms, they're automatically uploaded to Cloudinary
- **Image URLs**: Django generates Cloudinary URLs for your images
- **Optimization**: Cloudinary automatically optimizes images for web delivery
- **Storage**: All media files are stored in your Cloudinary account

## Cloudinary Dashboard Features

Once set up, you can:

- View all uploaded images in your Cloudinary Media Library
- Transform images on-the-fly using URL parameters
- Monitor bandwidth and storage usage
- Set up automatic backups
- Configure CDN settings

## Image Transformation (Optional)

You can transform images using Cloudinary's URL API. For example, in templates:

```django
<!-- Resize to 800px width -->
<img src="{{ project.featured_image.url }}?w_800" alt="{{ project.title }}">

<!-- Crop to 400x300 -->
<img src="{{ project.featured_image.url }}?c_fill,w_400,h_300" alt="{{ project.title }}">

<!-- Auto-format and quality -->
<img src="{{ project.featured_image.url }}?f_auto,q_auto" alt="{{ project.title }}">
```

## Free Tier Limits

- **Storage**: 25 GB
- **Bandwidth**: 25 GB/month
- **Transformations**: Unlimited
- **Video**: 25 GB storage, 25 GB bandwidth

For most portfolio websites, the free tier is more than sufficient!

## Troubleshooting

### Images not uploading
- Verify your Cloudinary credentials are correct
- Check that environment variables are set
- Look for errors in Django logs

### Images not displaying
- Check Cloudinary dashboard to verify images were uploaded
- Verify CLOUDINARY_CLOUD_NAME is correct
- Check browser console for 404 errors

### Exceeded quota
- Check your usage in Cloudinary dashboard
- Free tier resets monthly
- Consider upgrading if needed

## Security Notes

- **Never commit** your API secret to version control
- Always use environment variables for credentials
- `.env` file is already in `.gitignore`
- For production, set credentials in Render environment variables

## Resources

- Cloudinary Documentation: https://cloudinary.com/documentation
- Django Cloudinary Storage: https://github.com/klis87/django-cloudinary-storage
- Cloudinary Dashboard: https://cloudinary.com/console

---

**Your media files are now stored in the cloud!** ☁️

