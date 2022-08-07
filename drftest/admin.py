from django.contrib import admin
from .models import Coordination,Client

# Register your models here.


class Client_admin(admin.ModelAdmin):
    list_display=['name','mbti']  
admin.site.register(Client,Client_admin)

class Coordination_admin(admin.ModelAdmin):
    list_display=['client','top','bottom','shoes']
admin.site.register(Coordination,Coordination_admin)