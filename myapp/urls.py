from django.conf.urls import url
from django.urls import path
from myapp import views
app_name='myapp'
urlpatterns = [
                       url(r'^$', views.index, name='index'),
                       url(r'^contact/$', views.contact, name='contact'),
                       url(r'^about/$', views.about, name='about'),
                       url(r'^user/$', views.user, name='user'),
                       url(r'^form_view/$', views.form_view, name='form_view'),
                       url(r'^signup/$', views.signup, name='signup'),
                       url(r'^Register/$', views.Register, name='Register'),
                       url(r'^user_login/$', views.user_login, name='user_login'),
                       url(r'^user_logout/$', views.user_logout, name='user_logout'),
                       url(r'^special/$', views.special, name='special'),
]
