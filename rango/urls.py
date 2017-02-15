from django.conf.urls import url
from rango import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
<<<<<<< HEAD
	url(r'^add_category/$', views.add_category, name='add_category'),
=======
>>>>>>> ef14ed875835620051c6b4260340198a41e2c8ad
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
	views.show_category, name='show_category'),
]
