from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView

# def index_view(request):
#     return render(request,'index.html')
    

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

@login_required
def index_view(request):
    return render(request, 'index.html')