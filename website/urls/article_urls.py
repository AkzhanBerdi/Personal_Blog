# import sys
# sys.path.append("..")
from django.urls import path

from ..views.article_views import (
    article_create_view, 
    article_list_view,
    article_detail_view,
    article_update_view, 
    article_delete_view,
    ArticleDetailView,
)

from ..views.comment_views import CommentView


urlpatterns = [
    path('add',article_create_view, name='article_create'),
    path('list',article_list_view, name='article_list'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('update/<int:pk>', article_update_view, name='article_update'),
    path('delete/<int:pk>', article_delete_view, name='article_delete'),
    path('detail/<int:article_pk>/comments/add', CommentView.as_view(), name='add_comment'),
]