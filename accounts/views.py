from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserCreateForm


class SignupView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = UserCreateForm

    def get_success_url(self):
        return reverse_lazy('accounts:login')
