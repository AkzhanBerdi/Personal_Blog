from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, DetailView

from .forms import DjangoRegisterForm
from .models import Profile


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name='accounts/login.html')

    def post(self, request, *args, **kwargs):
        context = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            next = request.GET.get('next')
            if next:
                return redirect('next')
            return redirect('main')
        else:
            context['han_error'] = True
        return render(request, template_name='account/login.html', context=context)

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        next = request.Get.get('next')
        if next:
            return redirect(next)
        return redirect('accounts:login')


class RegisterView(CreateView):
    model = User
    template_name = 'accounts/registration.html'
    form_class = DjangoRegisterForm

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next = self.request.GET.get('next')
        if not next:
            next = self.request.POST.get('next')
        if not next:
            next = reverse('main')
        return next 


class UserDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'accounts/user_detail.html'
    context_object_name = 'user_obj'
    paginate_by = 5
    paginate_orphans = 0

    def get_context_data(self, **kwargs):
        articles = self.object.article.order_by('-created_at')
        paginator = Paginator(articles, self.paginate_by, orphans=self.paginate_orphans)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        kwargs['page_obj'] = page
        kwargs['articles'] = page.object_list
        kwargs['is_paginated'] = page.has_other_pages()
        return super().get_context_data(**kwargs)