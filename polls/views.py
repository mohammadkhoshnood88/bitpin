from .models import News , UserNews
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import NewsSerializer, ChoiceSerializer
from rest_framework import viewsets
from django.template import loader
from django.http import HttpResponse



def news(request):
    news = News.objects.all()
    template = loader.get_template("polls/index.html")
    context = {
        "news": news,
    }
    return HttpResponse(template.render(context, request))



def store_score(request , news_id , score):
    user = str(request.user)
    user = 1
    last_score = UserNews.objects.filter(user_id=user).filter(news_id=news_id)

    if len(last_score) > 0:
        last_score.update(score = score)
    else:
        UserNews.objects.create(news_id=news_id,score=score,user_id=user)
    


# class NewsViewSet(viewsets.ModelViewSet):
#     print("asdfasdf")
#     serializer_class = NewsSerializer
#     queryset = News.objects.all()


# class UserViewSet(viewsets.ModelViewSet):
#     serializer_class = ChoiceSerializer
#     queryset = User.objects.all()