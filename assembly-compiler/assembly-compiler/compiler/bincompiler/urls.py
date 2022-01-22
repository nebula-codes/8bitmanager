from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:code_id>/detail', views.detail, name='detail'),
    path('<int:code_id>/compile', views.compile, name='compile'),
    path('manage', views.manage, name='manage'),

]