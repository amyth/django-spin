from django.db import models

from django.utils.translation import ugettext as _


class Store(models.Model):
    name = models.CharField(_('name'), max_length=140)


class Featured(models.Model):
    title = models.CharField(_('title'), max_length=50)
    subtitle = models.CharField(_('subtitle'), max_length=100)
    image = models.ImageField(upload_to='media/images/featured/')
    url = models.CharField(_('url'), max_length=240)

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        verbose_name_plural = _('Featured')
