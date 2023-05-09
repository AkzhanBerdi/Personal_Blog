# import sys
# sys.path.append("..")
from django.urls import path

from ..views.genre_views import (
    genre_create_view, 
    genre_list_view
)

urlpatterns =[
    path('add', genre_create_view, name='genre_create'),
    path('list', genre_list_view, name='genre_list'),
]