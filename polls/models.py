from django.db import models
# from django.contrib.auth.models import User



class News(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
    def mean_score(self):
        scores = UserNews.objects.filter(news_id = self.id)
        mean = 0
        for score in scores:
            mean += score
        return mean / len(scores)

# this class is not use, we should use User model from contrib.models
class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)



class UserNews(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    news_id = models.ForeignKey(News,on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.user_id