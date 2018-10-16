from api.views import ArticlesViewSet
from django.conf.urls import re_path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'articles', ArticlesViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls))
]