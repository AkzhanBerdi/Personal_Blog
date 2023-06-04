from django.urls import path
from .views import LoginView, LogoutView, RegisterView, UserDetailView

app_name = 'accounts'

urlpatterns = [
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('register', RegisterView.as_view(), name="user_registration"),
    path('<int:pk>', UserDetailView.as_view(), name='user_detail')

]