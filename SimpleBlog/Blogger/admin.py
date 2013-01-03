from django.contrib import admin
from Blogger.models import Tag, Post, Author

class TagAdmin(admin.ModelAdmin):
	list_display = ('name', 'number_of_uses')

class PostAdmin(admin.ModelAdmin):
	exclude = ('author',)
	list_display = ('title', 'author', 'created_at', 'published', 'get_tags')
	list_filter = ['author', 'created_at', 'published']

	#http://stackoverflow.com/questions/753704/manipulating-data-in-djangos-admin-panel-on-save
	def save_model(self, request, obj, form, change):
		"""Customize save method via admin panel save"""
		if not obj.id:
			obj.author = request.user.author_set.all()[0]
		obj.set_slug()
		obj.save()


class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'user', 'number_of_posts')

class CommentAdmin(admin.ModelAdmin):
	pass

admin.site.register(Tag, TagAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Author, AuthorAdmin)
