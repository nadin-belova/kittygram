from django.urls import include, path
# from cats.views import CatList, CatDetail

from rest_framework.routers import DefaultRouter
from cats.views import CatViewSet


router = DefaultRouter()
router.register('cats', CatViewSet)  # basename='tiger'
# router.register('tigers', CatViewSet)

urlpatterns = [
   path('', include(router.urls)),
]
