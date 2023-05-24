from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from website.models import Author
from website.forms import AuthorForm

class AuthorView(CreateView):
    model = Author
    template_name = 'authors/create.html'
    form_class = AuthorForm
    success_url = reverse_lazy('author_list')
 
    def get_context_data(self, **kwargs):
        context = super().get_context(**kwargs)
        context['link'] = reverse('author_create')
        return context


class AuthorListView(ListView):
    template_name = 'authors/list.html'
    model = Author
    context_key = 'authors'
    paginate_by = 5
    paginate_orphans = 1


class AuthorListView(ListView):
    template_name = 'authors/list.html'
    model = Author
    context_key = 'authors'
    paginate_by = 5
    paaginate_orphans = 1


class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'authors/update.html'
    form_class = AuthorForm
    success_url = reverse_lazy('author_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['link'] = reverse('author_create')
        return context
    
class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('author_list')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)