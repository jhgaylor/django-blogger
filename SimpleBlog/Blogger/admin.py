from django.contrib import admin
from Blogger.models import Tag, Post, Author, Comment

class PostAdmin(admin.ModelAdmin):
	exclude = ('author',)

	#this makes the author of a post the user that created it.
	#http://stackoverflow.com/questions/753704/manipulating-data-in-djangos-admin-panel-on-save
	def save_model(self, request, obj, form, change):
		if not obj.id:
			obj.author = request.user.author_set.all()[0]
		obj.save()

admin.site.register(Tag)
admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Comment)
