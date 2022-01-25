from django.contrib import admin
from .models import Article
from .models import ArticleCategory, ArticleTag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass

@admin.register(ArticleCategory)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(ArticleTag)
class ArticleAdmin(admin.ModelAdmin):
    pass