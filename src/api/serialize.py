from rss_agregator.models import Article
from rest_framework import serializers


class ArticlesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'link', 'created', 'trend')