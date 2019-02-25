from rest_framework import serializers
from .models import Topic, HelpfulTopic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'title', 'text')

class HelpfulTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpfulTopic
        fields = ('id', 'user', 'topic', 'helpful')
