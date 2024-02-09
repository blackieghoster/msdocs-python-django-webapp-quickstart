from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello', views.hello, name='hello'),
    path('all', views.all_users, name='all_users'),
    path('add_user', views.add_user, name='add_user')
]
