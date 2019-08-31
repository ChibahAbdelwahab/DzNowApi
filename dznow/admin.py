from django.contrib import admin
from django import forms
from .models import News

class NewsAdminForm(forms.ModelForm):

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ['title', 'resume', 'content', 'date', 'author', 'category', 'image', 'source', 'link', 'video']
    readonly_fields = ['title', 'resume', 'content', 'date', 'author', 'category', 'image', 'source', 'link', 'video']

admin.site.register(News, NewsAdmin)


