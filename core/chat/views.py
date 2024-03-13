from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from .forms import UserRegistrationForm

# Create your views here.

"""
    this view shows the messages and redirects the user to login page if not logged in
"""
def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('login-user')
    context = {}
    return render(request, 'chat/chat-page.html', context)


"""
    this view is the registration view which users use to sign up
"""
class MySignUpView(CreateView):
    template_name = 'register.html'
    success_url = reverse_lazy("login-user")
    form_class = UserRegistrationForm
    success_message = "User created successfully"
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse("chat-page"))
        return super().dispatch(request, *args, **kwargs)
    