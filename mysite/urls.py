from . import views
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.post_list,name='post_list'),
    #url(r'^about/',views.about_site,name='about'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)