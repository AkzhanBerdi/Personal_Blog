from django.shortcuts import render
from django.views.generic import TemplateView

# def index_view(request):
#     return render(request,'index.html')
    

class IndexView(TemplateView):
    template_name = 'index.html'
    extra_context = {'hello': 'Hello, World!'}