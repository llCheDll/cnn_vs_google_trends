from django.db import models
from django.utils.translation import gettext as _


class Article(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_('Title')
    )
    
    link = models.URLField(
        max_length=1000,
        unique=True,
        verbose_name=_('Link')
    )
    
    created = models.DateTimeField(
        auto_now=False,
        verbose_name=_('Created at')
    )

    trend = models.CharField(
        max_length=1000,
        unique=True,
        verbose_name=_('Trend')
    )
    
    class Meta:
        db_table = 'article'
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
        