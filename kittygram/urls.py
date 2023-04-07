from django.urls import include, path

from cats.views import APICat, one_cat  # , cat_list


urlpatterns = [
   # path('cats/', cat_list),
   path('cats/', APICat.as_view()),
   path('cats/<int:pk>/', one_cat)
]
