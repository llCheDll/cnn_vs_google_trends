from rest_framework import viewsets
from api.serialize import ArticlesSerializer
from rss_agregator.models import Article


class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer
