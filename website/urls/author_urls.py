# import sys
# sys.path.append("..")
from django.urls import path

from ..views.author_views import (
    author_create_view,
    author_update_view,
    author_list_view
)

urlpatterns = [
    path('add', author_create_view, name='author_create'),
    path('update/<int:pk>', author_update_view, name='author_update'),
    path('list', author_list_view, name='author_list'),
]
