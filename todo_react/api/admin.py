from django.contrib import admin
from .models import Task

# Register your models here.
admin.site.register(Task)


admin.site.site_title = "Todo App Administration"
admin.site.site_header = "Todo App Administration"