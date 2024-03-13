from django.urls import path, include
from chat import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView
from .views import MySignUpView

urlpatterns = [
    # main page url
    path('', chat_views.chatPage, name='chat-page'),
    # login page url
    path('auth/login/', LoginView.as_view(template_name="chat/login.html"), name='login-user'),
    # logout page url
    path('auth/logout/', LogoutView.as_view(), name='logout-user'),
    # Sign up page url
    path('auth/register/', MySignUpView.as_view(), name='register-user'),
]
