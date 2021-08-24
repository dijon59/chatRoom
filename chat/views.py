from django.urls import reverse
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Message
from .forms import MessageForm


class MessageListView(LoginRequiredMixin, ListView):
    template_name = 'chat/chat-room.html'
    queryset = Message.objects.all()
    context_object_name = 'message_list'


class MessageCreateView(LoginRequiredMixin, CreateView):
    template_name = 'chat/create_message.html'
    form_class = MessageForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'chat/create_message.html'
    form_class = MessageForm
    model = Message


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message

    def get_success_url(self):
        return reverse('chat:message-list')
