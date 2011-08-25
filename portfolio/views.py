from django.views.generic.list_detail import object_detail, object_list
from models import Project, Skill, Category

__all__ = [
    'project_list',
    'project_detail',
    'category_detail',
    'skill_detail',
    ]

def project_context():
    return {
        'category_list': Category.objects.all(),
        'skill_list': Skill.objects.all(),
        }

def project_list(request, template_name='portfolio/project_list.html', extra_context={}):
    '''List of all projects.
    
    Renders fragments for each project.
    '''
    extra = project_context()
    extra.update(extra_context)
    extra['projects'] = Project.objects.all()
    return object_list(
        request,
        template_name = template_name,
        extra_context = extra,
        queryset = Category.objects.all(),
        )

def project_detail(request, slug, template_name='portfolio/project_detail.html', extra_context={}):
    '''Detail for the project with the given slug.'''
    extra = project_context()
    extra.update(extra_context)
    return object_detail(
        request,
        template_name = template_name,
        extra_context = extra,
        slug = slug,
        slug_field = 'slug',
        queryset = Project.objects.all(),
        )

def category_detail(request, slug, template_name='portfolio/category_detail.html', extra_context={}):
    '''List of projects in the category with the given slug.

    Renders fragments for each project.
    '''
    extra = project_context()
    extra.update(extra_context)
    return object_detail(
        request,
        template_name = template_name,
        extra_context = extra,
        slug = slug,
        slug_field = 'slug',
        queryset = Category.objects.all(),
        )

def skill_detail(request, slug, template_name='portfolio/skill_detail.html', extra_context={}):
    '''List of projects associated to the skill with the given slug.
    
    Renders fragments for each project.
    '''
    extra = project_context()
    extra.update(extra_context)
    return object_detail(
        request,
        template_name = template_name,
        extra_context = extra,
        slug = slug,
        slug_field = 'slug',
        queryset = Skill.objects.all(),
        )
