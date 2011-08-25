from django import template
from django.utils.safestring import mark_safe
from django.template.loader import get_template


register = template.Library()


@register.filter
def split(value, splitter):
    return value.split(splitter)


class HeaderForProjectNode(template.Node):
    def __init__(self, project_varname, should_link):
        self.project_var = template.Variable(project_varname)
        self.should_link = should_link == 'link'
    def render(self, context):
        project = self.project_var.resolve(context)
        t = get_template('portfolio/project_header.html')
        return t.render(template.Context({
            'project': project,
            'should_link': self.should_link,
        }))

@register.tag
def header_for_project(parser, token):
    '''Render the header for a project.
    
    Usage {%% header_for_project project [link] %%}
    '''
    try:
        tokens = token.split_contents()
        should_link = False
        if len(tokens) == 3:
            tag_name, project_varname, should_link = tokens
        else:
            tag_name, project_varname = tokens
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires two arguments" % token.contents.split()[0]
    return HeaderForProjectNode(project_varname, should_link)


class ProjectImageNode(template.Node):
    def __init__(self, project_varname):
        self.project_var = template.Variable(project_varname)
    def render(self, context):
        project = self.project_var.resolve(context)
        images = project.projectimage_set.all()
        if images.count() > 0:
            image = images[0]
            return mark_safe(
                u'<img class="project-image" src="%s" alt="%s" />' % (
                    image.image.url,
                    image.image.name.split('/')[-1],
                )
            )
        else:
            return u''

@register.tag
def image_for_project(parser, token):
    '''Render the first project image, if any.'''
    try:
        tag_name, project_varname = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires a single argument" % token.contents.split()[0]
    return ProjectImageNode(project_varname)