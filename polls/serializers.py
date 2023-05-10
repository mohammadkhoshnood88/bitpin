from rest_framework import serializers
from .models import News, User ,UserNews 

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields ='__all__'

class ChoiceSerializer(serializers.ModelSerializer):
    news = NewsSerializer
    class Meta:
        model = User
        fields ='__all__'