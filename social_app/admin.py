from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Report)
admin.site.register(Message)
admin.site.register(Friend_Request)