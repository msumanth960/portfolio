from django.shortcuts import render, get_object_or_404
import markdown
from .models import Project, Category, Analytics, Testimonial


def home(request):
    """Homepage with all sections"""
    featured_projects = Project.objects.filter(featured=True)[:6]
    all_projects = Project.objects.all()[:12]
    analytics = Analytics.objects.all()[:6]
    testimonials = Testimonial.objects.filter(featured=True)[:3]
    
    context = {
        'featured_projects': featured_projects,
        'projects': all_projects,
        'analytics': analytics,
        'testimonials': testimonials,
    }
    return render(request, 'portfolio/home.html', context)


def project_detail(request, slug):
    """Individual project detail page"""
    project = get_object_or_404(Project, slug=slug)
    related_projects = Project.objects.exclude(id=project.id)[:3]
    
    # Convert markdown to HTML
    markdown_html = ''
    if project.markdown_content:
        markdown_html = markdown.markdown(
            project.markdown_content,
            extensions=['fenced_code', 'tables', 'nl2br', 'sane_lists']
        )
    
    context = {
        'project': project,
        'related_projects': related_projects,
        'markdown_html': markdown_html,
    }
    return render(request, 'portfolio/project_detail.html', context)


def projects_list(request):
    """All projects listing page"""
    category_slug = request.GET.get('category')
    projects = Project.objects.all()
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        projects = projects.filter(category=category)
    
    categories = Category.objects.all()
    
    context = {
        'projects': projects,
        'categories': categories,
        'selected_category': category_slug,
    }
    return render(request, 'portfolio/projects_list.html', context)

