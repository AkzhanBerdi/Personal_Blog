from django.views import View
from django.shortcuts import get_object_or_404, redirect
from ..forms.genre_forms import CommentForm
from website.models import Article

class CommentView(View):
    def post(self,request,*args,**kwargs):
        form = CommentForm(request.POST)
        article_pk = kwargs.get('article_pk')
        if form.is_valid():
            article = get_object_or_404(Article, pk=article_pk)
            article.comments.create(
                text = request.POST.get('text'),
                author = request.POST.get('author'),
            )
        return redirect('article_detail', article_pk)