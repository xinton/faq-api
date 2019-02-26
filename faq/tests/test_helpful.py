"""
    Teste de API para requisições sobre Topicos
"""
from django.test import TestCase, Client
from django.urls import reverse
from model_mommy import mommy
from rest_framework import status
from ..models import HelpfulTopic, User, Topic
from ..serializers import HelpfulTopicSerializer

CLIENT = Client()


class TopicTest(TestCase):
    """ Test HelpfulTopic """

    def setUp(self):
        self.helpfulTopic_1 = mommy.make(HelpfulTopic)
        self.helpfulTopic_2 = mommy.make(HelpfulTopic)

        self.user_1 = mommy.make(User)

        self.topic_1 = mommy.make(Topic)

    # Casos de Sucesso
    def test_get_all_helpfulTopics(self):
        """
            Teste de requisição sobre a listagem de topicos uteis
        """
        response = CLIENT.get(reverse('helpfulTopics'))

        helpfulTopics = HelpfulTopic.objects.all()
        serializer = HelpfulTopicSerializer(helpfulTopics, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_helpfulTopic(self):
        """
            Teste da requisição para criação de topicos uteis
        """
        before = HelpfulTopic.objects.count()
        data = {'user': self.user_1.id,
                'topic': self.topic_1.id, 'helpful': True}

        response = CLIENT.post(reverse('helpfulTopics'), data, format='json')
        after = HelpfulTopic.objects.count()

        self.assertEqual(before, after - 1)
        self.assertEqual(after, before + 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_one_helpfulTopic(self):
        """
            Teste da requisição para obtenção de topico util
        """
        serializer = HelpfulTopicSerializer(self.helpfulTopic_1)
        response = CLIENT.get(reverse('helpfulTopic',
                                      args=[self.helpfulTopic_1.user.id,
                                            self.helpfulTopic_1.topic.id]))

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_helpfulTopic(self):
        """
            Teste da requisição para atualização de topico util
        """
        self.helpfulTopic_1.helpful = False
        serializer = HelpfulTopicSerializer(self.helpfulTopic_1)

        response = CLIENT.put(
            reverse('helpfulTopic', args=[
                    self.helpfulTopic_1.user.id,
                    self.helpfulTopic_1.topic.id]),
            serializer.data, content_type='application/json')

        self.assertEqual(response.data['helpful'], False)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_helpfulTopic(self):
        """
            Teste da requisição para remoção de topico util
        """
        before = HelpfulTopic.objects.count()
        response = CLIENT.delete(
            reverse('helpfulTopic',
                    args=[self.helpfulTopic_1.user.id,
                          self.helpfulTopic_1.topic.id]))
        after = HelpfulTopic.objects.count()

        self.assertEqual(before, after + 1)
        self.assertEqual(after, before - 1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # /FIM Casos de Sucesso

    # Casos de Falhas
    def test_get_one_helpfulTopic_that_does_not_exist(self):
        """
            Teste da requisição para obtenção de topico util que não existe
        """
        last_topic = Topic.objects.last()
        response = CLIENT.get(
            reverse('helpfulTopic', args=[self.helpfulTopic_1.user.id,
                                          last_topic.id+1]))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_remove_helpfulTopic_that_does_not_exist(self):
        """
            Teste da requisição para remoção de topico util que não existe
        """
        last_topic = Topic.objects.last()
        response = CLIENT.get(
            reverse('helpfulTopic', args=[self.helpfulTopic_1.user.id,
                                          last_topic.id+1]))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # /FIM Casos de Falhas
