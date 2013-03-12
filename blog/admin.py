from django.contrib import admin
from blog.models import *

class PostAdmin(admin.ModelAdmin):
	fields = (('title', 'slug'), 'body', 'author')
	prepopulated_fields = {'slug' : ('title', )}
	
	list_display = ('title', 'pub_date', 'author')
	list_filter = ['pub_date']
	search_fields = ['title']
	
admin.site.register(Post, PostAdmin)