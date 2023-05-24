from django.urls import path

from ..views.genre_views import (
    GenreListView, 
    GenreCreateView
)

urlpatterns =[
    path('add', GenreCreateView.as_view(), name='genre_create'),
    path('list', GenreListView.as_view(), name='genre_list'),
]