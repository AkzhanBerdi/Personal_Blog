from django.shortcuts import render, redirect, get_object_or_404
from website.models import Article, Author
from django.views import View
from ..forms.genre_forms import CommentForm
# from django.urls import reverse



def article_create_view(request):
    if request.method == 'GET':
        return render(
            request,
            'articles/create_article.html', 
            context={'authors': Author.objects.all()}
        )
    elif request.method == 'POST':
        author = get_object_or_404(Author, pk=request.POST.get('author_id'))
        article = Article.objects.create(
            title = request.POST.get('title'),
            author = author,
            body = request.POST.get('body')
        )

        return redirect('article_detail',pk=article.pk)


def article_list_view(request):
    articles = Article.objects.all()
    return render(request,'articles/article_list.html',context={
        'articles' : articles
    })


def article_detail_view(request, *args, **kwargs):
    article = get_object_or_404(Article, pk=kwargs.get('pk'))
    return render(request,'articles/article_detail.html', context={'article' : article})

class ArticleDetailView(View):

    def get(self, request, *args, **kwargs):
        form = CommentForm()
        return render(request, 'articles/article_detail.html', context={
            'article': get_object_or_404(Article,pk=kwargs.get('pk')),
            'form': form
            }
        )

def article_update_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        return render(request, 'articles/article_update.html', context={'article':article})
    elif request.method == 'POST':
        article.title = request.POST.get('title')
        article.author = request.POST.get('author')
        article.body = request.POST.get('body')
        article.save()
        return redirect('article_detail', pk=article.pk)


def article_delete_view(request,  pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        return render(request, 'articles/article_delete.html', context={'article':article})
    elif request.method =='POST':
        article.is_deleted = True
        article.save()
        return redirect('article_list')

