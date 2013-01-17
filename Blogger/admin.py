from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    """Admin panel class for Post"""
    exclude = ('author',)
    date_hierarchy = 'created_at'
    list_display = ('title', 'author', 'created_at', 'published', 'get_tags')
    list_filter = ['author', 'created_at', 'published']
    search_fields = ('title', 'body')
    prepopulated_fields = {"slug": ("title",)}

    #http://stackoverflow.com/questions/753704/manipulating-data-in-djangos-admin-panel-on-save
    def save_model(self, request, obj, form, change):
        """Customize save method via admin panel save"""
        if not change:
            obj.author = request.user
        #obj.set_slug()
        obj.save()


admin.site.register(Post, PostAdmin)
