from django.urls import path

from . import views

urlpatterns = [
    
    # ex: /polls
    path("", views.news, name="news"),

    path("<int:news_id>/score/<int:score>" , views.store_score)

    # ex: /polls/5/vote/
    # path("<int:news_id>/vote/", views.UserViewSet, name="vote"),
]