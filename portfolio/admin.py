from django.contrib import admin
from .models import Category, Project, ProjectImage, Analytics, Testimonial


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'icon']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'featured', 'order', 'created_at']
    list_filter = ['category', 'featured', 'created_at']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline]
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'category', 'featured', 'order')
        }),
        ('Content', {
            'fields': ('description', 'problem', 'solution', 'result', 'tech_stack', 'features', 'markdown_content')
        }),
        ('Media & Links', {
            'fields': ('featured_image', 'live_demo_url', 'github_url')
        }),
    )


@admin.register(Analytics)
class AnalyticsAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'description']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'company', 'rating', 'featured', 'order']
    list_filter = ['rating', 'featured', 'created_at']
    search_fields = ['client_name', 'company', 'content']

