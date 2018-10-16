from django.db import models
from django.utils.translation import gettext as _


class Article(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name=_('Title')
    )
    
    link = models.URLField(
        max_length=1000,
        verbose_name=_('Link')
    )
    
    created = models.CharField(
        max_length=100,
        verbose_name=_('Published')
    )

    trend = models.CharField(
        max_length=1000,
        verbose_name=_('Trend')
    )
    
    class Meta:
        db_table = 'article'
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
