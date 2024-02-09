from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello', views.hello, name='hello'),
    path('all', views.all_users, name='all_users'),
    path('add_user', views.add_user, name='add_user'),
    path('add_user_post', views.add_user_post, name='add_user_post')

]
