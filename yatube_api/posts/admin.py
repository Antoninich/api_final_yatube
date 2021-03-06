from django.contrib import admin

from .models import Comment, Follow, Group, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'author',
        'group',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    empty_value_display = '-пусто-'


admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(Group)
