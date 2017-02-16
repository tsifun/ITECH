from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')
<<<<<<< HEAD
class CategoryAdmin(admin.ModelAdmin):
     prepopulated_fields = {'slug':('name',)}
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
=======
<<<<<<< HEAD
class CategoryAdmin(admin.ModelAdmin):
     prepopulated_fields = {'slug':('name',)}
admin.site.register(Category, CategoryAdmin)
=======
<<<<<<< HEAD
class CategoryAdmin(admin.ModelAdmin):
     prepopulated_fields = {'slug':('name',)}
admin.site.register(Category, CategoryAdmin)
=======

admin.site.register(Category)
>>>>>>> 9792bf7070101d72b8fa1095987834bacc148344
>>>>>>> ef14ed875835620051c6b4260340198a41e2c8ad
admin.site.register(Page, PageAdmin)

>>>>>>> 494c4bd5839960f7c21e3ba2e673ddb51c4f95bb

# Register your models here.
