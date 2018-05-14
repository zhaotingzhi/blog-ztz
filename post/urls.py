from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^$',views.index_view),
    url(r'^page/(\d+)$',views.index_view),
    url(r'^post/(\d+)$',views.post_view),


]



















