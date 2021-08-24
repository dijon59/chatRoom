from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [
    path('', views.MessageListView.as_view(), name='message-list'),
    path('create-message/', views.MessageCreateView.as_view(), name='create-message'),
    path('update-message/<pk>', views.MessageUpdateView.as_view(), name='update-message'),
    path('delete-message/<pk>', views.MessageDeleteView.as_view(), name='delete-message'),
]
