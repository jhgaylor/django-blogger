from django.contrib import admin
from blogger.models import Post, Author


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
            obj.author = request.user.author_set.all()[0]
        #obj.set_slug()
        obj.save()


class AuthorAdmin(admin.ModelAdmin):
    """Admin panel class for Author"""
    list_display = ('first_name', 'last_name', 'user', 'number_of_posts')
    search_fields = ('first_name', 'last_name')

admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
