from django.urls import path
from faq import views

urlpatterns = [
    path('topics/', views.TopicList.as_view()),
    path('topics/<int:pk>/', views.TopicDetail.as_view()),
]