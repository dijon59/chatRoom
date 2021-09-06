from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserCreateForm
from chat.mails import send_welcome_email


class SignupView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = UserCreateForm

    def get_success_url(self):
        send_welcome_email(self.object)
        return reverse_lazy('accounts:login')
