from django.contrib import admin

# Register your models here.
from myapp.models import Topic,WebPage,AccessRecord,User_pro,UserProfileInfo
admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(AccessRecord)
admin.site.register(User_pro)
admin.site.register(UserProfileInfo)
