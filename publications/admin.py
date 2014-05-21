from django.contrib import admin

from django.contrib import admin
from publications.models import Author, Article, ArticleAuthors

# Register author admin
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email', 'organization')
    list_filter = ['organization']
    search_fields = ['last_name', 'first_name', 'email', 'organization']

admin.site.register(Author, AuthorAdmin)

# Register article admin

class AuthorInline(admin.TabularInline):
    model = ArticleAuthors
    extra = 3

class ArticleAdmin(admin.ModelAdmin):
    list_filter = ['submit_date']
    search_fields = ['headline']
    list_display = ('headline', 'submit_date')
    inlines = [AuthorInline]

admin.site.register(Article, ArticleAdmin)
