# import sys
# sys.path.append("..")
from django.shortcuts import render
from website.models import Genre
from ..forms.genre_forms import GenreForm
from django.shortcuts import redirect

def genre_list_view(request):
    return render(request, 'genre/genre_list.html', context ={'genres': Genre.objects.all()})

def genre_create_view(request):
    if request.method == 'GET':
        form = GenreForm()
        return render(request,'genre/genre_create.html', context={'form':form})
    elif request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            genre = Genre.objects.create(
                title = form.cleaned_data.get('title'),
                description = form.cleaned_data.get('description')
            )
            return redirect('genre_list')
        else:
            return render(request,'genre/genre_create.html', context={'form': form}) 