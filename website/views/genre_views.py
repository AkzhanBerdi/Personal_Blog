from django.urls import reverse_lazy
from website.models import Genre
from ..forms import GenreForm
from django.views.generic import ListView, CreateView

class GenreListView(ListView):
    template_name = 'genres/list.html'
    context_key = 'genres'
    model = Genre

class GenreCreateView(CreateView):
    model = Genre
    template_name = 'genres/create.html'
    form_class = GenreForm
    success_url = reverse_lazy('genre_list')