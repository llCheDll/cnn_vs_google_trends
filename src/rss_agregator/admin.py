from django.contrib import admin
from rss_agregator import models
from rss_agregator import forms


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    form = forms.ArticleForm
    