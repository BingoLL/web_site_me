from . import views
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.post_list,name='post_list'),
    url(r'^cate/(?P<cate_slug>[-\w]+)/$',views.post_list,name='post_list_by_cate'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$',views.post_list,name='post_list_by_tag'),
    url(r'^submit-comments/(?P<id>[0-9]+)/$',views.submit_comments,name='submit_comments'),
    url(r'^submit-messages/$',views.submit_message,name='submit_messages'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[0-9]+)/$',views.post_detail,name='post_detail'),
    url(r'^about/',views.about,name='about'),
    #url(r'^detail/',views.post_detail,name='post_detail_test'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)