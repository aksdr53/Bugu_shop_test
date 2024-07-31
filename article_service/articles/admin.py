from django.contrib import admin

from articles.models import User, Article


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email",)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
