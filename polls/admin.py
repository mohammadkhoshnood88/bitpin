from django.contrib import admin

from .models import News
from .models import User
from .models import UserNews

admin.site.register(News)
admin.site.register(User)
admin.site.register(UserNews)