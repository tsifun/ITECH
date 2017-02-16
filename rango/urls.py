from django.conf.urls import url
from rango import views

urlpatterns = [
<<<<<<< HEAD
    url(r'^$', views.index, name='index'),
    url(r'about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    url(r'^register/$', views.register, name='register'),
=======
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
<<<<<<< HEAD
	url(r'^add_category/$', views.add_category, name='add_category'),
=======
>>>>>>> ef14ed875835620051c6b4260340198a41e2c8ad
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
	views.show_category, name='show_category'),
>>>>>>> 494c4bd5839960f7c21e3ba2e673ddb51c4f95bb
]
