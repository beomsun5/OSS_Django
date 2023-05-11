from django.contrib import admin
from .models import Comment_duruduru, Comment_mochamilk

# Register your models here.
class CommentD(admin.ModelAdmin):
  search_fields = ['content']

class CommentM(admin.ModelAdmin):
  search_fields = ['content']

admin.site.register(Comment_duruduru, CommentD)
admin.site.register(Comment_mochamilk, CommentM)