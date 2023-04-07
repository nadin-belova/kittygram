from django.urls import include, path

from cats.views import cat_list, one_cat


urlpatterns = [
   path('cats/', cat_list),
   path('cats/<int:pk>/', one_cat)
]
