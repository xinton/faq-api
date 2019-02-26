from .models import Topic, HelpfulTopic
from .serializers import TopicSerializer, HelpfulTopicSerializer
from rest_framework import generics
from django.http import Http404


class TopicList(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class HelpfulTopicList(generics.ListCreateAPIView):
    queryset = HelpfulTopic.objects.all()
    serializer_class = HelpfulTopicSerializer


class HelpfulTopicDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        get: Obtem a opção do usuario(foi util ou não) para o topico especifico
    """
    def get_object(self):
        """
            Sobrescrevendo `get_object` para obter a instancia,
            se baseando no usuario e topico especifico
        """
        try:
            print(self.kwargs['topic_pk'])
            return HelpfulTopic.objects.get(
                user=self.kwargs['user_pk'], topic=self.kwargs['topic_pk'])
        except HelpfulTopic.DoesNotExist:
            raise Http404

    queryset = HelpfulTopic.objects.all()
    serializer_class = HelpfulTopicSerializer
