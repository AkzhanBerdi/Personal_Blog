from django.shortcuts import render, redirect, get_object_or_404
from website.models import Author, Article
from django.urls import reverse


def author_create_view(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    author = Author(first_name=first_name, last_name=last_name)
    errors = {}

    if first_name and len(first_name) > 50:
        errors['first_name'] = 'Too many characters' 
    if last_name and len(last_name) > 50:
        errors['last_name'] = 'Too many characters' 

    if request.method == 'GET':
        return render(
            request,
            'authors/create_author.html', 
            context={'link': reverse('author_create')
            }
        )
    elif request.method == 'POST':
        if not errors:
            author = Author.objects.create(
                first_name = first_name,
                last_name = last_name,
            )

            return redirect('author_list')
        else:
            return render(
                request,
                'authors/create_author.html',
                context = {'errors': errors, 'author': author}
            )


def author_list_view(request):
    author = Author.objects.all()
    return render(request, 'authors/author_list.html', context={'author': author})


def author_update_view(request, pk):
    author = get_object_or_404(Author,pk=pk)

    if request.method == 'GET':
        return render(
            request, 
            'authors/author_update.html', 
            context={
                'author': author,
                'link': reverse('author_update', kwargs={'pk': pk})
            }
        )
    elif request.method == 'POST':

        author.first_name = request.POST.get('first_name')
        author.last_name = request.POST.get('last_name')
        
        errors = {}
        if author.first_name and len(author.first_name) > 50:
            errors['first_name'] = 'Too many characters' 
        if author.last_name and len(author.last_name) > 50:
            errors['last_name'] = 'Too many characters' 
        
        if not errors:
            author.save()
            return redirect('author_list')
        
        elif errors:
            return render(
                request, 
                'authors/author_update.html', 
                context={
                    'author': author,
                    'link': reverse('author_update', kwargs={'pk': pk}),
                    'errors': errors
                }
            )