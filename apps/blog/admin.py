from django.contrib import admin

from apps.blog.models import Article, Project, FAQ


admin.site.register(Article)
admin.site.register(Project)
admin.site.register(FAQ)