from django.contrib import admin
from BookApp.models import Book1,  Topic, Post

# Register your models here.

admin.site.register(Book1)
admin.site.register(Topic)
admin.site.register(Post)