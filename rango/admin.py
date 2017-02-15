from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')
<<<<<<< HEAD
class CategoryAdmin(admin.ModelAdmin):
     prepopulated_fields = {'slug':('name',)}
admin.site.register(Category, CategoryAdmin)
=======

admin.site.register(Category)
>>>>>>> 9792bf7070101d72b8fa1095987834bacc148344
admin.site.register(Page, PageAdmin)


# Register your models here.
