"""
    Teste de API para requisições sobre Topicos
"""
from django.test import TestCase, Client
from django.urls import reverse
from model_mommy import mommy
from rest_framework import status
from ..models import Topic
from ..serializers import TopicSerializer

CLIENT = Client()


class TopicTest(TestCase):
    """ Test Topic """

    def setUp(self):
        self.topic_1 = mommy.make(Topic)
        self.topic_2 = mommy.make(Topic)

    # Casos de Sucesso
    def test_get_all_topics(self):
        """
            Teste de requisição sobre a listagem de topicos
        """
        response = CLIENT.get(reverse('topics'))

        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_topic(self):
        """
            Teste da requisição para criação de topicos
        """
        before = Topic.objects.count()
        data = {'title': 'NOVO', 'text': 'DETAIL'}

        response = CLIENT.post(reverse('topics'), data, format='json')
        after = Topic.objects.count()

        self.assertEqual(before, after - 1)
        self.assertEqual(after, before + 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_one_topic(self):
        """
            Teste da requisição para obtenção de topico
        """
        serializer = TopicSerializer(self.topic_1)

        response = CLIENT.get(reverse('topic', args=[self.topic_1.id]))

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_topic(self):
        """
            Teste da requisição para atualização de topico
        """
        self.topic_1.text = 'ATUALIZADO'
        serializer = TopicSerializer(self.topic_1)

        response = CLIENT.put(
            reverse('topic', args=[self.topic_1.id]),
            serializer.data, content_type='application/json')

        self.assertEqual(response.data['text'], 'ATUALIZADO')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_topic(self):
        """
            Teste da requisição para remoção de topico
        """
        before = Topic.objects.count()
        response = CLIENT.delete(
            reverse('topic', args=[self.topic_2.id]))
        after = Topic.objects.count()

        self.assertEqual(before, after + 1)
        self.assertEqual(after, before - 1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # /FIM Casos de Sucesso

    # Casos de Falhas
    def test_get_one_topic_that_does_not_exist(self):
        """
            Teste da requisição para obtenção de topico que não existe
        """
        last_topic = Topic.objects.last()
        response = CLIENT.get(
            reverse('topic', args=[last_topic.id + 1]))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_remove_topic_that_does_not_exist(self):
        """
            Teste da requisição para remoção de topico que não existe
        """
        last_topic = Topic.objects.last()
        response = CLIENT.get(
            reverse('topic', args=[last_topic.id + 1]))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # /FIM Casos de Falhas
