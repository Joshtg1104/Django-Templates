from django.urls import path

from . import views
# paths for all the end points
urlpatterns = [
    path('index/', views.index, name='index'),
    path('index/base/', views.base, name='base'),
    path('index/about/', views.about, name='about'),
]
