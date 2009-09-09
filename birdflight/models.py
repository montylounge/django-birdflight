from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

class Project(models.Model):

    codename = models.CharField(_('codename'), max_length=100, unique=True, null=True)
    slug = models.SlugField()
    description = models.TextField(_('description'), blank=True, null=True)

    class Meta:
        verbose_name = _('project')
        verbose_name_plural = _('projects')

    def __unicode__(self):
        return self.codename

    def save(self):
        self.slug = slugify(self.codename)
        super(Project, self).save()

