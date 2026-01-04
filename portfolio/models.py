from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Project categories"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text="Bootstrap icon class")

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class Project(models.Model):
    """Portfolio projects"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='projects')
    description = models.TextField()
    problem = models.TextField(help_text="The problem this project solves")
    solution = models.TextField(help_text="How this project solves the problem")
    result = models.TextField(help_text="Results and impact")
    tech_stack = models.CharField(max_length=500, help_text="Comma-separated list of technologies")
    features = models.TextField(blank=True, help_text="Key features of the project (one per line or comma-separated)")
    markdown_content = models.TextField(blank=True, help_text="Additional project details in Markdown format")
    featured_image = models.ImageField(upload_to='projects/', blank=True, null=True)
    live_demo_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False, help_text="Show on homepage")
    order = models.IntegerField(default=0, help_text="Display order")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def get_tech_list(self):
        """Return tech stack as a list"""
        return [tech.strip() for tech in self.tech_stack.split(',') if tech.strip()]
    
    def get_features_list(self):
        """Return features as a list"""
        if not self.features:
            return []
        # Support both line breaks and comma-separated
        features = self.features.replace('\n', ',').split(',')
        return [feature.strip() for feature in features if feature.strip()]

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})


class ProjectImage(models.Model):
    """Additional images for projects"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.project.title} - Image {self.order}"


class Analytics(models.Model):
    """Analytics showcase items"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='analytics/', blank=True, null=True)
    insights = models.TextField(help_text="Key insights from this analytics")
    impact = models.CharField(max_length=500, help_text="Business impact or results")
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Analytics"
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    """Client testimonials"""
    client_name = models.CharField(max_length=100)
    client_title = models.CharField(max_length=200, blank=True)
    company = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    rating = models.IntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return f"{self.client_name} - {self.rating} stars"

