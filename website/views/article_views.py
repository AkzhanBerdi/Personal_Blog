from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import urlencode
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView

from website.models import Article, Author, Tag
from ..helpers.views import CustomDeleteView, CustomCreateView, CustomUpdateView
from ..forms import ArticleForm, SearchFrom




class ArticleCreateView(CustomCreateView):
    template_name = 'articles/create.html'
    form_class = ArticleForm
    model = Article
    

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.all()
        context['tags'] = Tag.objects.all()
        return context

    def get_redirect_url(self):
        return reverse('article_detail',kwargs={'pk':self.object.pk})


class ArticleListView(ListView):
    model = Article
    context_key = 'articles'
    template_name = 'articles/list.html'
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 1
    form = SearchFrom

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return self.form(self.request.GET)

    def get_serach_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search:': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().getquery_set()
        if self.search_value:
            query = Q(title__icontains=self.search_value) | Q(author__first_name__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

def article_detail_view(request, *args, **kwargs):
    article = get_object_or_404(Article, pk=kwargs.get('pk'))
    return render(request,'articles/detail.html', context={'article' : article})

class ArticleDetailView(DetailView):
    template_name = 'articles/detail.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.object
        comments = article.comments.order_by('-created_at')
        context['comment'] = comments
        return context


class ArticleUpdateView(CustomUpdateView):
    template_name = 'articles/update.html'
    form_class = ArticleForm
    model = Article
    context_object_name = 'article'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = Author.objects.all()
        return context

    def get_redirect_url(self):
        return reverse('article_detail', kwargs={'pk': self.object.pk})


class ArticleDeleteView(CustomDeleteView):
    template_name = 'articles/delete.html'
    model = Article
    context_key = 'article'

    def get_redirect_url(self):
        return reverse_lazy('article_list')