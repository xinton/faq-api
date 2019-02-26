from django.urls import path
from faq import views

urlpatterns = [
    path('topics/', views.TopicList.as_view(), name='topics'),
    path('topics/<int:pk>/', views.TopicDetail.as_view(), name='topic'),
    path('helpfultopics/', views.HelpfulTopicList.as_view()),
    path('helpfultopics/<int:user_pk>/<int:topic_pk>/',
         views.HelpfulTopicDetail.as_view()),
]
