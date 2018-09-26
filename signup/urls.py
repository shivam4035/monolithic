from sys import path

from django.conf.urls import include, url
from . import views

urlpatterns = [

    url(r'^$', views.signUP, name='signup'),
    url('MNNIT_KART.html/$', views.about, name='kart'),
    url(r'^home/$', views.signin, name='signin'),
    url(r'^register/$', views.register, name='register'),
    url(r'^welcome/$', views.home, name='home'),
    url(r'^home/MNNIT_KART.html/$', views.about, name='kart'),
    url(r'^home/upload.html/$', views.upload, name='upload'),
    url(r'^welcome/MNNIT_KART.html/$', views.about, name='kart'),
    url(r'^welcome/upload.html/$', views.upload, name='upload'),
    url(r'^added/$', views.add, name='additem'),
    url(r'^dash/$', views.item_detail, name='collect'),
    url(r'^dash/upload.html/$', views.upload, name='dash_upload'),
    url('logout/$',views.signout,name='signout'),
    url('books/$',views.books,name='books'),
    url('books/upload.html',views.upload,name='upload'),
    url('cycle/$',views.cycle,name='cycle'),
    url('cycle/upload.html',views.upload,name='upload'),
    url('cooler/$',views.cooler,name='cooler'),
    url('cooler/upload.html',views.upload,name='upload'),
    url('all/$',views.item_detail,name='all'),
    url('all/upload.html',views.upload,name='upload'),
]