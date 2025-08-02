from django.contrib.auth import views as auth_views
from django.urls import include, path
from . import views


app_name = 'journey'

urlpatterns = [
    path('', views.journey_list, name='journey_list'),
    path(
        '<int:journey_id>/',
        views.journey_detail,
        name='journey_detail'
    ),
    path(
        'create/',
        views.journey_create,
        name='journey_create'
    ),
    path(
        'profile/<str:username>/',
        views.profile,
        name='profile'
    ),
]
