# import sys
# sys.path.append("..")
from django.urls import path

from ..views.article_views import (
    article_create_view, 
    article_list_view,
    article_detail_view,
    article_update_view, 
    article_delete_view
)


urlpatterns = [
    path('add',article_create_view, name='article_create'),
    path('list',article_list_view, name='article_list'),
    path('detail/<int:pk>', article_detail_view, name='article_detail'),
    path('update/<int:pk>', article_update_view, name='article_update'),
    path('delete/<int:pk>', article_delete_view, name='article_delete'),

]