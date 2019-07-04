from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'search',views.search_titles,name='search_titles'),
    path('<int:num>/',views.result,name='result'),
    path('search_result',views.result,name='result'),
]