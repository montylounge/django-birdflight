from django.template import RequestContext
from birdflight.models import Project
from django.views.generic import list_detail
from django.shortcuts import render_to_response

def homepage(request, template_name='birdflight/home.html', extra_context=None):
    '''Displays project list.'''

    project = Project.objects.all().order_by('?')[0]

    extra = { 'project': project }

    if extra_context:
        extra.update(extra_context)

    return render_to_response(template_name, extra, context_instance=RequestContext(request))

